#!/usr/bin/env python3
"""Three-layer scorer for the multi-file application corpus.

A single confusion matrix cannot describe what these artifacts test. A tool that
finds a SQL injection but has no idea the value came from another service is not
the same as a tool that traced it, and a tool that finds three of five planted
weaknesses is not the same as a tool that found none. So the score is a triple,
reported side by side and never averaged into one number that hides which of the
three a tool is actually bad at.

  Layer 1 -- flow judgment.  Unit: one declared flow. Did the tool decide
  correctly whether this path is exploitable? Sanitized-but-broken paths are
  scored separately as well, because that sub-metric is what separates a tool
  modelling what a sanitizer does from one matching that a sanitizer was called.
  Reported as Youden's J = sensitivity + specificity - 1, so guessing "everything
  is vulnerable" scores 0 rather than 50%.

  Layer 2 -- CWE identification.  Unit: a flow the tool already got right at
  layer 1. Naming the exact CWE scores 1.0; naming its parent scores 0.5;
  anything else scores 0. Conditioned on layer 1 so a tool cannot farm CWE points
  by reporting every CWE at every line.

  Layer 3 -- chain reconstruction.  Unit: the application. How much of the
  service graph did the tool recover, and did it identify the weakness at the
  entry that makes the rest reachable? Recovering the path is worth double when
  the entry is also named, because that combination is the whole question: not
  "is there a bug here" but "how do these bugs compose into an escalation".

  A tool is charged a layer-3 false positive for claiming a completed chain in an
  application where a control on the path holds. Those applications contain every
  individual weakness the vulnerable twin does; the only difference is that the
  chain is blocked.

Anti-gaming: layer 3 is only counted for an application whose layer-1 J clears
MIN_J1_FOR_LAYER3. Reconstructing a graph you cannot judge is not understanding.

The ground truth is the two CSVs a multi-file suite ships beside its code: the
flows CSV (``--flows``) and the chains CSV (``--chains``). ``--selftest`` runs
the built-in checks, including a round trip through both CSV layouts.

Usage:
    score_apps.py --flows <expectedresults-V.csv> --chains <expectedresults-chains-V.csv> --tool-sarif <file.sarif>
    score_apps.py --selftest
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from pathlib import Path

#: Recovering the chain is worth double when the entry weakness is also named.
PUZZLE_BONUS = 1.0

#: Layer 3 is not counted for an application whose layer-1 J is below this.
MIN_J1_FOR_LAYER3 = 0.5

#: A reported line this far from the expected one still matches. Tools legitimately
#: differ on whether a multi-line call site starts at the receiver or the argument.
LINE_TOLERANCE = 2

UNSANITIZED = "UNSANITIZED"
SANITIZED_BROKEN = "SANITIZED_BROKEN"
SANITIZED_EFFECTIVE = "SANITIZED_EFFECTIVE"

#: CWE -> genuine hierarchy parent, for the layer-2 half-credit tier.
#:
#: Every edge here is a real ChildOf in MITRE's Research Concepts view (view 1000),
#: verified individually against cwe.mitre.org. The table is static so the scorer
#: needs nothing installed beside it, and half credit is only ever given for a
#: true taxonomic parent: a chain's entry CWE is not a parent of its impact CWE.
#: When adding an edge, it MUST be a ChildOf in view 1000.
_CWE_HIERARCHY_PARENT: dict[int, int] = {
    78: 77,    # OS Command Injection -> Command Injection
    79: 74,    # Cross-site Scripting -> Injection
    83: 79,    # Script in Attributes -> Cross-site Scripting
    89: 943,   # SQL Injection -> Improper Neutralization in Data Query Logic
    862: 285,  # Missing Authorization -> Improper Authorization
    22: 706,   # Path Traversal -> Use of Incorrectly-Resolved Name or Reference
    502: 913,  # Deserialization of Untrusted Data -> Improper Control of Dynamically-Managed Code Resources
    269: 284,  # Improper Privilege Management -> Improper Access Control
    200: 668,  # Exposure of Sensitive Information -> Exposure of Resource to Wrong Sphere
    639: 863,  # Authorization Bypass Through User-Controlled Key -> Incorrect Authorization
}


# --------------------------------------------------------------------------
# Corpus + tool loading
# --------------------------------------------------------------------------


@dataclass
class Corpus:
    flows: list[dict] = field(default_factory=list)
    apps: list[dict] = field(default_factory=list)
    parent_cwe: dict[int, int] = field(default_factory=dict)


# --------------------------------------------------------------------------
# Public answer key (the two CSVs a multi-file suite ships)
# --------------------------------------------------------------------------

#: Column order of ``expectedresults-<version>.csv`` for a multi-file suite: one
#: row per declared flow and one per front door, after four ``# `` comment lines.
FLOWS_CSV_COLUMNS = (
    "key", "category", "vulnerable", "cwe", "kind", "truth",
    "app_id", "archetype", "service", "file", "line",
)

#: Column order of ``expectedresults-chains-<version>.csv``: one row per edge per
#: artifact in edge order, or one row with the edge columns empty for an artifact
#: that declares no edge, after one ``# `` header line.
CHAINS_CSV_COLUMNS = (
    "app_id", "archetype", "edge_index", "from_node", "from_service", "from_file",
    "to_node", "to_service", "to_file", "boundary", "entry_service", "entry_file",
    "entry_cwe", "entry_weakness_real", "impact_cwe", "chain_completes", "planted_cwes",
)

#: The ``kind`` of a front-door row. It is not a flow: the weakness is the absence
#: of a control, scored at layer 3 off the chain row rather than matched at layer 1.
ENTRY_KIND = "entry"
ENTRY_WEAKNESS = "ENTRY_WEAKNESS"
ENTRY_CONTROLLED = "ENTRY_CONTROLLED"
ENTRY_CATEGORY = "entry_weakness"


def _csv_rows(text: str, width: int) -> list[list[str]]:
    """Data rows of a public CSV: comment and blank lines dropped, each row split
    positionally and padded to ``width`` so a trailing empty column survives."""
    rows: list[list[str]] = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split(",")]
        if len(parts) < width:
            parts.extend([""] * (width - len(parts)))
        rows.append(parts)
    return rows


def _int_or_none(text: str) -> int | None:
    return int(text) if text.strip() else None


def public_corpus_from_text(flows_text: str, chains_text: str) -> Corpus:
    """The Corpus the three layers score, built from the two public CSVs.

    Every field the three layers read is recovered: flows with ``flow_id``,
    ``cwe``, ``verdict``, ``expects_finding``, ``sink_path`` and ``sink_line``;
    artifacts with ``app_id``, ``archetype``, their services (node index, name and
    primary file, read off the edge rows), the chain (edges, entry CWE, whether the
    entry weakness is real, whether the chain completes), the planted CWEs and
    their own flows grouped on ``app_id``. Front-door rows are not flows and are
    left out of the flow list.
    """
    corpus = Corpus(parent_cwe=dict(_CWE_HIERARCHY_PARENT))
    apps: dict[str, dict] = {}
    for row in _csv_rows(chains_text, len(CHAINS_CSV_COLUMNS)):
        r = dict(zip(CHAINS_CSV_COLUMNS, row))
        app = apps.get(r["app_id"])
        if app is None:
            app = apps[r["app_id"]] = {
                "app_id": r["app_id"],
                "archetype": r["archetype"] or None,
                "services": [],
                "flows": [],
                "planted_cwes": [int(c) for c in r["planted_cwes"].split(";") if c],
                "chain": {
                    "edges": [],
                    "entry_cwe": _int_or_none(r["entry_cwe"]),
                    "entry_weakness_real": r["entry_weakness_real"] == "true",
                    "impact_cwe": _int_or_none(r["impact_cwe"]),
                    "completes": r["chain_completes"] == "true",
                },
            }
        if not r["edge_index"]:
            continue
        nodes = {s["node_index"]: s for s in app["services"]}
        for idx_col, svc_col, file_col in (
            ("from_node", "from_service", "from_file"), ("to_node", "to_service", "to_file"),
        ):
            idx = int(r[idx_col])
            nodes.setdefault(idx, {"node_index": idx, "service": r[svc_col] or None, "path": r[file_col]})
        app["services"] = [nodes[k] for k in sorted(nodes)]
        app["chain"]["edges"].append(
            {"from_node": int(r["from_node"]), "to_node": int(r["to_node"]), "boundary": r["boundary"]}
        )
    for row in _csv_rows(flows_text, len(FLOWS_CSV_COLUMNS)):
        r = dict(zip(FLOWS_CSV_COLUMNS, row))
        if r["kind"] == ENTRY_KIND:
            continue
        flow = {
            "flow_id": r["key"],
            "category": r["category"],
            "cwe": int(r["cwe"]),
            "verdict": r["truth"],
            "expects_finding": r["vulnerable"] == "true",
            "kind": r["kind"],
            "service": r["service"],
            "sink_path": r["file"],
            "sink_line": int(r["line"] or 0),
            "hops": [],
            "edges": [],
        }
        corpus.flows.append(flow)
        app = apps.get(r["app_id"])
        if app is not None:
            app["flows"].append(flow)
    corpus.apps = list(apps.values())
    if not corpus.flows and not corpus.apps:
        raise SystemExit("no ground truth in the public CSVs: expected at least one flow row or one chain row")
    return corpus


def load_public_corpus(flows_csv: Path, chains_csv: Path) -> Corpus:
    """Read the public answer key of one multi-file suite: its flows CSV
    (``expectedresults-<version>.csv``) and chains CSV
    (``expectedresults-chains-<version>.csv``)."""
    return public_corpus_from_text(
        flows_csv.read_text(encoding="utf-8"), chains_csv.read_text(encoding="utf-8"),
    )


def _entry_location(app: dict) -> tuple[str, str, int]:
    """(service, file, line) of an artifact's front door: its lowest-index
    service and the first hop line there, or line 1 when no hop lands on it."""
    services = sorted(app.get("services") or [], key=lambda s: int(s.get("node_index") or 0))
    if not services:
        return "", "", 1
    entry = services[0]
    node_index = int(entry.get("node_index") or 0)
    path = str(entry.get("path") or "")
    lines = [
        int(hop.get("line") or 0)
        for flow in app.get("flows") or ()
        for hop in flow.get("hops") or ()
        if hop.get("node_index") == node_index and hop.get("path") == path
    ]
    live = [ln for ln in lines if ln > 0]
    return str(entry.get("service") or ""), path, (min(live) if live else 1)


def _csv_line(values) -> str:
    cells = ["" if v is None else str(v) for v in values]
    for cell in cells:
        if "," in cell or "\n" in cell:
            raise ValueError(f"a public CSV value may not contain a comma or a newline: {cell!r}")
    return ",".join(cells)


def public_csv_text(
    corpus: Corpus, version: str = "selftest", suite_name: str = "selftest",
    language: str = "", framework: str = "", shape: str = "application",
) -> tuple[str, str]:
    """The two public CSV layouts for a Corpus: (flows CSV text, chains CSV text).

    The selftest serialises its in-memory corpus through this and loads it
    back through ``public_corpus_from_text``, so the loader is proved against the
    layout rather than against itself.
    """
    flow_app: dict[str, dict] = {}
    for app in corpus.apps:
        for flow in app.get("flows") or []:
            flow_app[str(flow.get("flow_id"))] = app
    flows = corpus.flows or [fl for app in corpus.apps for fl in (app.get("flows") or [])]
    rows: list[str] = []
    for flow in flows:
        app = flow_app.get(str(flow.get("flow_id")), {})
        rows.append(_csv_line((
            flow.get("flow_id"), flow.get("category") or "",
            "true" if flow.get("expects_finding") else "false",
            int(flow.get("cwe") or 0), flow.get("kind") or "primary", flow.get("verdict") or "",
            app.get("app_id") or "", app.get("archetype") or "", flow.get("service") or "",
            flow.get("sink_path") or "", int(flow.get("sink_line") or 0),
        )))
    for app in corpus.apps:
        chain = app.get("chain") or {}
        if not chain.get("entry_cwe"):
            continue
        real = bool(chain.get("entry_weakness_real", True))
        service, path, line = _entry_location(app)
        rows.append(_csv_line((
            f"{app.get('app_id')}:entry", ENTRY_CATEGORY, "true" if real else "false",
            int(chain["entry_cwe"]), ENTRY_KIND, ENTRY_WEAKNESS if real else ENTRY_CONTROLLED,
            app.get("app_id") or "", app.get("archetype") or "", service, path, line,
        )))
    flows_lines = [
        "# " + ",".join(FLOWS_CSV_COLUMNS),
        f"# {suite_name} v{version}",
        f"# {len(rows)} test cases, dataset {version}",
        f"# language={language} framework={framework} shape={shape}",
        *rows,
    ]
    chain_lines = ["# " + ",".join(CHAINS_CSV_COLUMNS)]
    for app in corpus.apps:
        chain = app.get("chain") or {}
        by_node = {s.get("node_index"): s for s in app.get("services") or []}
        entry_service, entry_file, _line = _entry_location(app)
        planted = sorted(int(c) for c in (app.get("planted_cwes") or []) if c)
        tail = (
            entry_service, entry_file,
            "" if chain.get("entry_cwe") is None else int(chain["entry_cwe"]),
            "true" if chain.get("entry_weakness_real", True) else "false",
            "" if chain.get("impact_cwe") is None else int(chain["impact_cwe"]),
            "true" if chain.get("completes") else "false",
            ";".join(str(c) for c in planted),
        )
        head = (app.get("app_id") or "", app.get("archetype") or "")
        edges = chain.get("edges") or []
        if not edges:
            chain_lines.append(_csv_line(head + ("",) * 8 + tail))
            continue
        for i, e in enumerate(edges):
            src = by_node.get(e["from_node"], {})
            dst = by_node.get(e["to_node"], {})
            chain_lines.append(_csv_line(head + (
                i, e["from_node"], src.get("service") or "", src.get("path") or "",
                e["to_node"], dst.get("service") or "", dst.get("path") or "", e.get("boundary") or "",
            ) + tail))
    return "\n".join(flows_lines) + "\n", "\n".join(chain_lines) + "\n"


@dataclass
class ToolFinding:
    path: str
    line: int
    cwe: int | None
    key: str
    hops: tuple[tuple[str, int], ...] = ()


def load_tool_sarif(path: Path) -> list[ToolFinding]:
    """Flatten a tool's SARIF into (path, line, cwe, recovered hops)."""
    data = json.loads(path.read_text(encoding="utf-8"))
    out: list[ToolFinding] = []
    for run in data.get("runs") or []:
        for res in run.get("results") or []:
            loc = (res.get("locations") or [{}])[0]
            phys = loc.get("physicalLocation") or {}
            uri = (phys.get("artifactLocation") or {}).get("uri", "")
            line = (phys.get("region") or {}).get("startLine", 0)
            out.append(ToolFinding(
                path=uri,
                line=int(line or 0),
                cwe=_rule_to_cwe(res.get("ruleId")),
                key=str((res.get("properties") or {}).get("testCaseKey", "")),
                hops=_sarif_hops(res),
            ))
    return out


def _rule_to_cwe(rule_id) -> int | None:
    if rule_id is None:
        return None
    text = str(rule_id).strip().upper().replace("CWE-", "")
    digits = "".join(c for c in text if c.isdigit())
    return int(digits) if digits else None


def _sarif_hops(result: dict) -> tuple[tuple[str, int], ...]:
    hops: list[tuple[str, int]] = []
    for cf in result.get("codeFlows") or []:
        for tf in cf.get("threadFlows") or []:
            for tfl in tf.get("locations") or []:
                phys = ((tfl.get("location") or {}).get("physicalLocation") or {})
                uri = (phys.get("artifactLocation") or {}).get("uri", "")
                line = (phys.get("region") or {}).get("startLine", 0)
                if uri:
                    hops.append((uri, int(line or 0)))
    return tuple(hops)


# --------------------------------------------------------------------------
# Layer 1 + 2
# --------------------------------------------------------------------------


@dataclass
class LayerOneResult:
    tp: int = 0
    fp: int = 0
    tn: int = 0
    fn: int = 0
    broken_expected: int = 0
    broken_found: int = 0
    matched: list[tuple[dict, ToolFinding]] = field(default_factory=list)

    @property
    def sensitivity(self) -> float:
        pos = self.tp + self.fn
        return self.tp / pos if pos else 0.0

    @property
    def specificity(self) -> float:
        neg = self.tn + self.fp
        return self.tn / neg if neg else 0.0

    @property
    def youden_j(self) -> float:
        """Youden's J, generalised to the one-sided case.

        J is ``sensitivity + specificity - 1``, which is the same thing as
        ``2 * balanced_accuracy - 1``. Written the second way it stays defined
        when a subset has only one class in it -- which is the normal case for a
        single application, where every flow may be vulnerable. The first form
        silently reads that as specificity 0 and reports J = 0 for a tool that
        got everything right, which then trips the layer-3 anti-gaming guard on
        exactly the applications a good tool solved. Identical arithmetic
        whenever both classes are present, so the corpus-wide number is unchanged.
        """
        recalls = []
        if self.tp + self.fn:
            recalls.append(self.sensitivity)
        if self.tn + self.fp:
            recalls.append(self.specificity)
        if not recalls:
            return 0.0
        return 2.0 * (sum(recalls) / len(recalls)) - 1.0

    @property
    def broken_sanitizer_recall(self) -> float:
        return self.broken_found / self.broken_expected if self.broken_expected else 0.0


def _matches(flow: dict, finding: ToolFinding) -> bool:
    """Whether a tool finding lands on a flow's terminal operation."""
    if finding.key and finding.key == flow.get("flow_id"):
        return True
    expected_path = flow.get("sink_path") or ""
    if not expected_path or not finding.path:
        return False
    if not (finding.path.endswith(expected_path) or expected_path.endswith(finding.path)):
        return False
    expected_line = int(flow.get("sink_line") or 0)
    if not expected_line or not finding.line:
        return True
    return abs(finding.line - expected_line) <= LINE_TOLERANCE


def score_layer_one(
    flows: list[dict], findings: list[ToolFinding], is_entry_weakness=None,
) -> LayerOneResult:
    """Judge every declared flow, then charge whatever the tool reported besides.

    ``is_entry_weakness`` exempts one class of unmatched finding from the false
    positive charge: the weakness at the chain's entry. That weakness is real and
    deliberately planted, but it is the ABSENCE of a control rather than a path
    from a source to a sink, so it has no flow to match against and is scored at
    layer 3 instead. Without the exemption a tool would be penalised at layer 1
    for the very finding layer 3 rewards. The exemption is narrow: the finding
    must name that application's declared entry CWE, lie inside that application,
    and the application must actually HAVE the weakness -- so it cannot be farmed
    by reporting the CWE everywhere, and it does not excuse claiming a missing
    control on a front door that has one.
    """
    res = LayerOneResult()
    unclaimed = list(findings)
    for flow in flows:
        expects = bool(flow.get("expects_finding"))
        verdict = flow.get("verdict")
        if verdict == SANITIZED_BROKEN:
            res.broken_expected += 1
        hit = next((f for f in unclaimed if _matches(flow, f)), None)
        if hit is not None:
            unclaimed.remove(hit)
        if expects:
            if hit is not None:
                res.tp += 1
                res.matched.append((flow, hit))
                if verdict == SANITIZED_BROKEN:
                    res.broken_found += 1
            else:
                res.fn += 1
        else:
            if hit is not None:
                res.fp += 1
            else:
                res.tn += 1
    # Findings that matched nothing in the ground truth are false positives on
    # code the corpus declares safe or unscored. Charging them is the point of
    # emitting benign modules at all.
    for leftover in unclaimed:
        if is_entry_weakness is not None and is_entry_weakness(leftover):
            continue
        res.fp += 1
    return res


def score_layer_two(matched, parent_cwe: dict[int, int]) -> tuple[float, int, int, int]:
    """(accuracy, exact, parent, wrong) over the layer-1 true positives."""
    exact = parent = wrong = 0
    for flow, finding in matched:
        truth = int(flow.get("cwe") or 0)
        if finding.cwe == truth:
            exact += 1
        elif finding.cwe is not None and parent_cwe.get(truth) == finding.cwe:
            parent += 1
        else:
            wrong += 1
    total = exact + parent + wrong
    score = (exact + 0.5 * parent) / total if total else 0.0
    return score, exact, parent, wrong


# --------------------------------------------------------------------------
# Layer 3
# --------------------------------------------------------------------------


@dataclass
class LayerThreeResult:
    scored_apps: int = 0
    skipped_apps: int = 0
    total_score: float = 0.0
    chain_fp: int = 0
    chain_tn: int = 0
    entry_hits: int = 0
    cwe_recall_apps: int = 0
    cwe_recall_total: float = 0.0
    planted_cwes: int = 0
    planted_cwes_found: int = 0

    @property
    def score(self) -> float:
        return self.total_score / self.scored_apps if self.scored_apps else 0.0

    @property
    def cwe_recall(self) -> float:
        """Mean share of an application's planted CWEs the tool named.

        Contract section 2.3 states this as an explicit, separately reported
        number and gives the reason: an application carries 3 to 5 unrelated
        weaknesses, so a tool that finds 4 of 5 is not the same as one that finds
        none, and the corpus has to be able to say so. It is deliberately NOT
        folded into ``chain_score`` -- the contract scores it "regardless of chain
        outcome", so a blocked application still contributes.
        """
        return self.cwe_recall_total / self.cwe_recall_apps if self.cwe_recall_apps else 0.0


def _recovered_edges(app: dict, findings: list[ToolFinding]) -> set[tuple[int, int]]:
    """Edges the tool demonstrated it followed, via its own thread flows.

    An edge counts as recovered when a reported path contains a location in the
    upstream service's file and a later location in the downstream service's file.
    Naming both files in unrelated findings is not recovery: the ordered pair
    inside one path is the evidence that the tool connected them.
    """
    node_paths = {s["node_index"]: s["path"] for s in app.get("services") or []}
    recovered: set[tuple[int, int]] = set()
    for finding in findings:
        ordered: list[int] = []
        for uri, _line in finding.hops:
            for idx, path in node_paths.items():
                if uri.endswith(path) or path.endswith(uri):
                    if not ordered or ordered[-1] != idx:
                        ordered.append(idx)
                    break
        for a, b in zip(ordered, ordered[1:]):
            recovered.add((a, b))
    return recovered


def score_layer_three(
    apps: list[dict], findings: list[ToolFinding], j1_by_app: dict[str, float],
) -> LayerThreeResult:
    res = LayerThreeResult()
    for app in apps:
        chain = app.get("chain") or {}
        true_edges = {(e["from_node"], e["to_node"]) for e in chain.get("edges") or []}
        if not true_edges:
            continue
        app_findings = _findings_in_app(app, findings)
        recovered = _recovered_edges(app, app_findings)
        claims_chain = bool(recovered & true_edges)

        # Partial credit over the application's planted weaknesses, before the
        # completes/blocked split: contract 2.3 scores this "regardless of chain
        # outcome", so a blocked application's four other CWEs still count. Behind
        # the same anti-gaming guard as the chain score, because a tool that
        # reports every CWE everywhere would otherwise farm it -- and a tool that
        # sprays findings has already tanked its layer-1 J.
        planted = {int(c) for c in (app.get("planted_cwes") or []) if c}
        if planted and j1_by_app.get(app["app_id"], 0.0) >= MIN_J1_FOR_LAYER3:
            hit = planted & {f.cwe for f in app_findings if f.cwe is not None}
            res.cwe_recall_apps += 1
            res.cwe_recall_total += len(hit) / len(planted)
            res.planted_cwes += len(planted)
            res.planted_cwes_found += len(hit)

        if not chain.get("completes"):
            # Blocked chain. There is nothing to reconstruct and a claim that the
            # path is open is a false positive at this layer.
            if claims_chain:
                res.chain_fp += 1
            else:
                res.chain_tn += 1
            continue

        if j1_by_app.get(app["app_id"], 0.0) < MIN_J1_FOR_LAYER3:
            res.skipped_apps += 1
            continue

        edge_recall = len(recovered & true_edges) / len(true_edges)
        entry_cwe = chain.get("entry_cwe")
        entry_bit = 1 if entry_cwe and any(f.cwe == entry_cwe for f in app_findings) else 0
        res.entry_hits += entry_bit
        res.scored_apps += 1
        res.total_score += edge_recall * (1 + PUZZLE_BONUS * entry_bit)
    return res


def _findings_in_app(app: dict, findings: list[ToolFinding]) -> list[ToolFinding]:
    prefix = app.get("app_id") or ""
    if not prefix:
        return findings
    out = []
    for f in findings:
        paths = [f.path] + [h[0] for h in f.hops]
        if any(prefix in p for p in paths):
            out.append(f)
    return out


def _entry_weakness_predicate(apps: list[dict]):
    """A finding is the entry weakness when it names an app's declared entry CWE
    AND lies inside that app AND that app actually has the weakness. All three are
    required. The CWE alone would let a tool report it across the whole corpus for
    free, and exempting it on an app whose front door carries a working control
    would excuse a real false positive: reporting missing authorization on an
    authorized endpoint is wrong, and the exemption existed only because the
    finding has no flow to be matched against when it IS right."""
    pairs = [
        (app.get("app_id") or "", (app.get("chain") or {}).get("entry_cwe"))
        for app in apps
        # Default True for an answer key written before the column existed: silence
        # there means "unknown", and the old behaviour is the safer reading.
        if (app.get("chain") or {}).get("entry_weakness_real", True)
    ]
    pairs = [(prefix, cwe) for prefix, cwe in pairs if prefix and cwe]
    if not pairs:
        return None

    def predicate(finding: ToolFinding) -> bool:
        paths = [finding.path] + [h[0] for h in finding.hops]
        return any(
            finding.cwe == cwe and any(prefix in p for p in paths)
            for prefix, cwe in pairs
        )

    return predicate


def _j1_by_app(corpus: Corpus, findings: list[ToolFinding]) -> dict[str, float]:
    out: dict[str, float] = {}
    for app in corpus.apps:
        flows = app.get("flows") or []
        if not flows:
            continue
        out[app["app_id"]] = score_layer_one(
            flows, _findings_in_app(app, findings), _entry_weakness_predicate([app]),
        ).youden_j
    return out


# --------------------------------------------------------------------------
# Report
# --------------------------------------------------------------------------


def score(corpus: Corpus, findings: list[ToolFinding]) -> dict:
    flows = corpus.flows or [fl for app in corpus.apps for fl in (app.get("flows") or [])]
    l1 = score_layer_one(flows, findings, _entry_weakness_predicate(corpus.apps))
    l2_score, exact, parent, wrong = score_layer_two(l1.matched, corpus.parent_cwe)
    l3 = score_layer_three(corpus.apps, findings, _j1_by_app(corpus, findings))
    return {
        "layer1": {
            "tp": l1.tp, "fp": l1.fp, "tn": l1.tn, "fn": l1.fn,
            "sensitivity": round(l1.sensitivity, 4),
            "specificity": round(l1.specificity, 4),
            "youden_j": round(l1.youden_j, 4),
            "broken_sanitizer_recall": round(l1.broken_sanitizer_recall, 4),
            "broken_sanitizer_flows": l1.broken_expected,
        },
        "layer2": {
            "accuracy": round(l2_score, 4),
            "exact": exact, "parent": parent, "wrong": wrong,
            "parent_map_loaded": bool(corpus.parent_cwe),
        },
        "layer3": {
            "score": round(l3.score, 4),
            "apps_scored": l3.scored_apps,
            "apps_skipped_low_j1": l3.skipped_apps,
            "entry_weakness_hits": l3.entry_hits,
            "blocked_chain_true_negatives": l3.chain_tn,
            "blocked_chain_false_positives": l3.chain_fp,
            # Reported beside the chain score, never averaged into it. The two
            # answer different questions: how much of the graph did the tool
            # recover, and how many of the weaknesses planted along it did it name.
            "cwe_recall": round(l3.cwe_recall, 4),
            "cwe_recall_apps": l3.cwe_recall_apps,
            "planted_cwes": l3.planted_cwes,
            "planted_cwes_found": l3.planted_cwes_found,
        },
        "triple": [
            round(l1.youden_j, 4), round(l2_score, 4), round(l3.score, 4),
        ],
    }


def render(report: dict) -> str:
    l1, l2, l3 = report["layer1"], report["layer2"], report["layer3"]
    out = [
        "=== Layer 1: flow judgment ===",
        f"  TP {l1['tp']}  FP {l1['fp']}  TN {l1['tn']}  FN {l1['fn']}",
        f"  sensitivity {l1['sensitivity']:.4f}  specificity {l1['specificity']:.4f}",
        f"  Youden J    {l1['youden_j']:.4f}",
        f"  broken-sanitizer recall {l1['broken_sanitizer_recall']:.4f} "
        f"over {l1['broken_sanitizer_flows']} flows",
        "",
        "=== Layer 2: CWE identification ===",
        f"  accuracy {l2['accuracy']:.4f}  (exact {l2['exact']}, parent {l2['parent']}, wrong {l2['wrong']})",
    ]
    if not l2["parent_map_loaded"]:
        out.append("  NOTE: parent-CWE map unavailable; a parent answer scored 0, not 0.5")
    out += [
        "",
        "=== Layer 3: chain reconstruction ===",
        f"  score {l3['score']:.4f} over {l3['apps_scored']} apps",
        f"  planted-CWE recall {l3['cwe_recall']:.4f} over {l3['cwe_recall_apps']} apps "
        f"({l3['planted_cwes_found']} of {l3['planted_cwes']} planted weaknesses named)",
        f"  entry weakness identified in {l3['entry_weakness_hits']} apps",
        f"  blocked chains: {l3['blocked_chain_true_negatives']} correct, "
        f"{l3['blocked_chain_false_positives']} falsely claimed complete",
        f"  apps skipped for layer-1 J below {MIN_J1_FOR_LAYER3}: {l3['apps_skipped_low_j1']}",
        "",
        "TRIPLE (J1, A2, S3): %.4f  %.4f  %.4f" % tuple(report["triple"]),
    ]
    return "\n".join(out)


# --------------------------------------------------------------------------
# Self-test
# --------------------------------------------------------------------------


def _selftest_corpus() -> Corpus:
    hops = [
        {"path": "app/a.py", "line": 10, "service": "intake", "node_index": 0,
         "role": "source", "kind": "read", "boundary": None},
        {"path": "app/a.py", "line": 12, "service": "intake", "node_index": 0,
         "role": "source", "kind": "send", "boundary": "http"},
        {"path": "app/b.py", "line": 8, "service": "ledger", "node_index": 1,
         "role": "sink", "kind": "receive", "boundary": "http"},
        {"path": "app/b.py", "line": 9, "service": "ledger", "node_index": 1,
         "role": "sink", "kind": "sink", "boundary": None},
    ]
    open_flow = {
        "flow_id": "App0001", "cwe": 89, "verdict": UNSANITIZED,
        "expects_finding": True, "sink_path": "app/b.py", "sink_line": 9,
        "hops": hops,
        "edges": [{"from_node": 0, "to_node": 1, "boundary": "http"}],
    }
    safe_flow = {
        "flow_id": "App0001_b00", "cwe": 89, "verdict": SANITIZED_EFFECTIVE,
        "expects_finding": False, "sink_path": "app/c.py", "sink_line": 5,
        "hops": [], "edges": [],
    }
    broken_flow = {
        "flow_id": "App0002", "cwe": 78, "verdict": SANITIZED_BROKEN,
        "expects_finding": True, "sink_path": "app/d.py", "sink_line": 21,
        "hops": [], "edges": [],
    }
    blocked_flow = {
        "flow_id": "App0003", "cwe": 89, "verdict": SANITIZED_EFFECTIVE,
        "expects_finding": False, "sink_path": "app/e.py", "sink_line": 4,
        "hops": [], "edges": [],
    }
    apps = [
        {
            "app_id": "app", "test_id": "00001",
            "services": [
                {"node_index": 0, "path": "app/a.py", "service": "intake"},
                {"node_index": 1, "path": "app/b.py", "service": "ledger"},
            ],
            "flows": [open_flow, safe_flow, broken_flow],
            # The weaknesses planted in this application, which is what layer 3's
            # partial credit is measured against: the sorted set of the CWEs of
            # its flows that expect a finding.
            "planted_cwes": [78, 89],
            "chain": {
                "edges": [{"from_node": 0, "to_node": 1, "boundary": "http"}],
                "gates": [], "entry_cwe": 306, "entry_weakness_real": True,
                "impact_cwe": 89, "completes": True,
            },
        },
        {
            "app_id": "blocked", "test_id": "00003",
            "services": [
                {"node_index": 0, "path": "blocked/a.py", "service": "intake"},
                {"node_index": 1, "path": "blocked/e.py", "service": "ledger"},
            ],
            "flows": [blocked_flow],
            "chain": {
                "edges": [{"from_node": 0, "to_node": 1, "boundary": "http"}],
                "gates": [{"node_index": 0, "control": "authz_decision"}],
                # Declared, and NOT present: the gate is on the entry node, so
                # this is the contrast case rather than a second weak door.
                "entry_cwe": 306, "entry_weakness_real": False,
                "impact_cwe": 89, "completes": False,
            },
        },
    ]
    return Corpus(
        flows=[open_flow, safe_flow, broken_flow, blocked_flow],
        apps=apps,
        parent_cwe={89: 943, 78: 77},
    )


def _perfect_findings() -> list[ToolFinding]:
    return [
        ToolFinding(path="app/b.py", line=9, cwe=89, key="App0001",
                    hops=(("app/a.py", 10), ("app/a.py", 12), ("app/b.py", 8), ("app/b.py", 9))),
        ToolFinding(path="app/d.py", line=21, cwe=78, key="App0002"),
        ToolFinding(path="app/x.py", line=1, cwe=306, key=""),
    ]


def run_selftest() -> int:
    corpus = _selftest_corpus()
    failures: list[str] = []

    perfect = _perfect_findings()
    # The entry weakness is reported as its own finding inside the app, exactly as
    # a tool that solved the puzzle would report it.
    perfect[2] = ToolFinding(path="app/entry.py", line=1, cwe=306, key="")
    rep = score(corpus, perfect)
    if rep["triple"][0] != 1.0:
        failures.append(f"perfect layer1 J = {rep['triple'][0]}, expected 1.0")
    if rep["triple"][1] != 1.0:
        failures.append(f"perfect layer2 accuracy = {rep['triple'][1]}, expected 1.0")
    if rep["triple"][2] != 2.0:
        failures.append(
            f"perfect layer3 = {rep['triple'][2]}, expected 2.0 "
            f"(full edge recall doubled by the entry-weakness bonus)"
        )
    if rep["layer1"]["broken_sanitizer_recall"] != 1.0:
        failures.append("perfect broken-sanitizer recall != 1.0")
    if rep["layer3"]["blocked_chain_true_negatives"] != 1:
        failures.append("perfect run did not credit the blocked chain as a true negative")
    if rep["layer3"]["cwe_recall"] != 1.0:
        failures.append(
            f"perfect planted-CWE recall = {rep['layer3']['cwe_recall']}, expected 1.0"
        )

    # The property the whole "3 to 5 planted CWEs" design exists for: a tool that
    # names one of the two planted weaknesses must score 0.5, not 0 and not 1.
    # Contract 2.3 calls this out explicitly, and nothing measured it.
    partial = score(corpus, [_perfect_findings()[0]])
    if partial["layer3"]["cwe_recall"] != 0.5:
        failures.append(
            f"partial planted-CWE recall = {partial['layer3']['cwe_recall']}, expected 0.5 "
            f"(one of two planted CWEs named)"
        )

    null = score(corpus, [])
    if null["triple"][0] != 0.0:
        failures.append(f"null-tool layer1 J = {null['triple'][0]}, expected 0.0")
    if null["triple"][2] != 0.0:
        failures.append(f"null-tool layer3 = {null['triple'][2]}, expected 0.0")
    if null["layer2"]["accuracy"] != 0.0:
        failures.append("null-tool layer2 accuracy is not 0.0")
    if null["layer1"]["fn"] != 2:
        failures.append(f"null-tool FN = {null['layer1']['fn']}, expected 2")

    # A tool that reports everything must not beat a tool that reports correctly.
    noisy = _perfect_findings() + [
        ToolFinding(path="app/c.py", line=5, cwe=89, key="App0001_b00"),
        ToolFinding(path="app/e.py", line=4, cwe=89, key="App0003"),
    ]
    noisy_rep = score(corpus, noisy)
    if noisy_rep["triple"][0] >= rep["triple"][0]:
        failures.append("firing on the safe flows did not reduce layer-1 J")
    if noisy_rep["layer3"]["blocked_chain_false_positives"] != 0:
        failures.append("a location-only finding was miscounted as a chain claim")

    # Claiming the entry weakness inside an app whose front door carries a working
    # control is an ordinary false positive, not a bonus. The exemption keyed on
    # the declared CWE alone, so every gated artifact excused it for free -- and
    # the corpus published `true` on all of them, which charged the tools that
    # were right and credited the ones that were not.
    misplaced = score(corpus, _perfect_findings()[:2] + [
        ToolFinding(path="blocked/a.py", line=1, cwe=306, key=""),
    ])
    if misplaced["layer1"]["fp"] != 1:
        failures.append(
            f"entry weakness claimed on a controlled front door scored "
            f"{misplaced['layer1']['fp']} false positives, expected 1"
        )

    # Claiming the blocked app's chain must be charged.
    claimer = _perfect_findings() + [
        ToolFinding(path="blocked/e.py", line=4, cwe=89, key="App0003",
                    hops=(("blocked/a.py", 3), ("blocked/e.py", 4))),
    ]
    claim_rep = score(corpus, claimer)
    if claim_rep["layer3"]["blocked_chain_false_positives"] != 1:
        failures.append("claiming a blocked chain was not charged as a layer-3 FP")

    # Naming the parent CWE instead of the exact one must score half.
    parented = [
        ToolFinding(path="app/b.py", line=9, cwe=943, key="App0001",
                    hops=(("app/a.py", 10), ("app/b.py", 9))),
        ToolFinding(path="app/d.py", line=21, cwe=78, key="App0002"),
    ]
    par_rep = score(corpus, parented)
    if par_rep["layer2"]["accuracy"] != 0.75:
        failures.append(
            f"parent-CWE accuracy = {par_rep['layer2']['accuracy']}, expected 0.75"
        )

    # An app whose flows are all vulnerable has no negative class. A tool that
    # judged every one of them correctly must not be treated as having J = 0 and
    # skipped by the layer-3 guard.
    one_sided = LayerOneResult(tp=3, fn=0, tn=0, fp=0)
    if one_sided.youden_j != 1.0:
        failures.append(
            f"one-sided perfect J = {one_sided.youden_j}, expected 1.0"
        )
    one_sided_bad = LayerOneResult(tp=0, fn=3, tn=0, fp=0)
    if one_sided_bad.youden_j != -1.0:
        failures.append(
            f"one-sided total-miss J = {one_sided_bad.youden_j}, expected -1.0"
        )
    both_sides = LayerOneResult(tp=3, fn=1, tn=2, fp=2)
    if abs(both_sides.youden_j - (0.75 + 0.5 - 1.0)) > 1e-9:
        failures.append("two-sided J no longer equals sensitivity + specificity - 1")

    # The CSV answer key must score exactly what the in-memory corpus scores:
    # serialise this corpus to the two shipped CSV layouts, load it back through
    # the public loader, and compare the triple for every tool exercised above.
    flows_text, chains_text = public_csv_text(corpus)
    public = public_corpus_from_text(flows_text, chains_text)
    for label, findings in (
        ("perfect", perfect), ("null", []), ("noisy", noisy),
        ("misplaced", _perfect_findings()[:2] + [ToolFinding(path="blocked/a.py", line=1, cwe=306, key="")]),
        ("claimer", claimer), ("parented", parented),
    ):
        want = score(corpus, findings)["triple"]
        got = score(public, findings)["triple"]
        if got != want:
            failures.append(
                f"public CSV round trip scores {got} for the {label} tool where the "
                f"in-memory corpus scores {want}"
            )
    if len(public.flows) != len(corpus.flows):
        failures.append(
            f"public CSV round trip recovered {len(public.flows)} flows from "
            f"{len(corpus.flows)} (front-door rows must not become flows)"
        )

    if failures:
        print("SELFTEST FAILED")
        for f in failures:
            print("  -", f)
        return 1
    print("SELFTEST PASSED")
    print()
    print(render(rep))
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--flows", type=Path, help="public flows CSV (expectedresults-<version>.csv); pair with --chains")
    ap.add_argument("--chains", type=Path, help="public chains CSV (expectedresults-chains-<version>.csv); pair with --flows")
    ap.add_argument("--tool-sarif", type=Path, help="the tool output to score")
    ap.add_argument("--json", action="store_true", help="emit the report as JSON")
    ap.add_argument("--selftest", action="store_true", help="run the built-in checks")
    args = ap.parse_args(argv)

    if args.selftest:
        return run_selftest()
    if not args.tool_sarif:
        ap.error("--tool-sarif is required unless --selftest is given")
    if bool(args.flows) != bool(args.chains):
        ap.error("--flows and --chains go together")
    if not args.flows:
        ap.error("--flows with --chains is required unless --selftest is given")

    corpus = load_public_corpus(args.flows, args.chains)
    findings = load_tool_sarif(args.tool_sarif)
    report = score(corpus, findings)
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(render(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
