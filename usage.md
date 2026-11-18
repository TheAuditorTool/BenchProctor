# Using BenchProctor

The operational guide: how to pick the bundle you want, run a scanner against it, and read the
score. For what the release is and why it is built the way it is, see [README.md](README.md); for
the release history, see [changelog.md](changelog.md).

The current release is `2026.11.16`: standalone cases, one file per case, in all 11 languages, and
60 multi-service applications.

## 1. Pick your bundle

A standalone bundle is one language. It holds every framework for that language, so you choose the
framework inside the bundle.

```
Benchmarks/standalone/benchproctor-<language>-2026.11.16.zip
Benchmarks/applications/benchproctor-applications-2026.11.16.zip
```

- "I want Java" -> `Benchmarks/standalone/benchproctor-java-2026.11.16.zip`, then the `spring/` or
  `jakarta/` framework subtree inside it.
- "I want Python, FastAPI" -> `Benchmarks/standalone/benchproctor-python-2026.11.16.zip`, then the
  `fastapi/` subtree.
- "I want the multi-service applications" ->
  `Benchmarks/applications/benchproctor-applications-2026.11.16.zip`, then one service-graph
  directory inside it.

The framework names for each language are listed in the README's
[Languages & frameworks](README.md#languages--frameworks) table.

## 2. What is inside a standalone bundle

Labels live only in the CSV answer keys. The test files themselves carry no comments, CWE tags, or
label-bearing names, so you cannot infer a label from a file.

```
benchproctor-<language>/
  score_sarif.py                     the scorer (standard-library Python, no dependencies)
  benchproctor-manifest.json         version, per-framework counts, SHA-256 checksums
  README.md                          bundle-local notes
  <framework>/
    testcode/                        the cases you scan
    expectedresults-2026.11.16.csv   the answer key for this framework
```

Some frameworks also carry the build files their toolchain needs next to `testcode/`, for example
`pom.xml` for Java. They hold no labels.

Compiling the C cases needs the development headers of SQLite, libcurl and OpenSSL, because the C
standard library has no SQL, HTTP or cryptography API. See
[C prerequisites](README.md#c-prerequisites) for the install commands.

## 3. Run and score a standalone framework

```bash
# extract
unzip Benchmarks/standalone/benchproctor-java-2026.11.16.zip -d benchproctor-java

# scan one framework's testcode and export SARIF 2.1.0
your-tool scan ./benchproctor-java/spring/testcode --format sarif -o results.sarif

# score against that framework's answer key
python ./benchproctor-java/score_sarif.py results.sarif \
  ./benchproctor-java/spring/expectedresults-2026.11.16.csv
```

The scorer matches a finding to a case by file and recovers the finding's CWE from the SARIF
`ruleId`, the result or rule `properties` or `tags` (for example `external/cwe/cwe-089`), or CWE
`taxa`. If your tool emits no CWE at all, add `--match-mode filename`: any finding on a vulnerable
file then counts. That mode rewards over-flagging, so prefer the default when your tool emits CWEs.

### Reading the output

The scorer prints a confusion matrix and, from it, three numbers:

- `TPR` (true-positive rate): the share of vulnerable cases your tool flagged.
- `FPR` (false-positive rate): the share of safe cases your tool flagged.
- `J` (Youden's J = TPR - FPR): the headline score.

`J` is reported two ways. **Category-averaged** weights each class equally, so a few large classes
cannot dominate; **flat aggregate** weights every case equally. A perfect tool scores `J = +100%`.
A flag-everything or flag-nothing tool scores `0%`, because its TPR and FPR are equal. A tool that
flags safe code and misses real bugs scores below zero.

Each framework holds 3 vulnerable and 3 safe cases per class. One class in one framework therefore
moves in steps of a third. Read scores per language, or per class across frameworks.

## 4. The applications bundle

```
benchproctor-applications/
  score_apps.py                             the scorer (standard-library Python, no dependencies)
  benchproctor-manifest.json                version, counts, SHA-256 checksums
  README.md                                 bundle-local notes
  <service-graph>/
    applications/<application>/             one project: docker-compose.yml and services/<service>/
    expectedresults-2026.11.16.csv          one row per labeled flow, with its file and line
    expectedresults-chains-2026.11.16.csv   the service graph and whether the chain completes
```

Scan a service graph's `applications/` directory as one tree, then score it:

```bash
unzip Benchmarks/applications/benchproctor-applications-2026.11.16.zip -d benchproctor-apps
your-tool scan ./benchproctor-apps/nestjs-spring/applications --format sarif -o results.sarif
python ./benchproctor-apps/score_apps.py \
  --flows  ./benchproctor-apps/nestjs-spring/expectedresults-2026.11.16.csv \
  --chains ./benchproctor-apps/nestjs-spring/expectedresults-chains-2026.11.16.csv \
  --tool-sarif results.sarif
```

The scorer reports a triple and never averages it into one number:

- **Flow judgment** (Youden's J): did the tool decide correctly whether each labeled flow is
  exploitable?
- **CWE identification**: for the flows it judged correctly, did it name the right CWE? The exact
  CWE scores 1, its parent in the CWE hierarchy scores a half.
- **Chain reconstruction**: how much of the service graph did the tool recover, and did it name the
  weakness at the entry that makes the rest reachable?

A finding matches a flow by file and line, with a tolerance of two lines.

## 5. Verify your download

Every published file is checksummed. From the `Benchmarks/` directory:

```bash
sha256sum -c SHASUMS256.txt
```

Per-file checksum sidecars accompany the bundles for spot verification.

## FAQ

**Why is the split exactly 50 / 50 vulnerable and safe?**
So a tool cannot game the score by flagging everything. Under Youden's J, a flag-everything tool has
a 100% true-positive rate and a 100% false-positive rate, which nets to zero. The applications are
not 50 / 50: most of the code in a real project is safe, and so it is there.

**Why is the release so small?**
It is a curated release. Three cases per side for each framework and class is enough to score a
language or a class, and each release is a fresh draw, so a tool cannot be tuned to the files.

**Does it test whether my tool understands a broken safeguard?**
No. In this release a vulnerable case has no safeguard and a safe case has one that works. See the
README's [What this release does not contain](README.md#what-this-release-does-not-contain).

**Can I train a model on the corpus?**
As with any benchmark, do not train on the exact corpus you then report a score against.

**My tool does not emit CWE identifiers. Can I still score?**
Yes, for the standalone cases: `--match-mode filename` counts any finding on a vulnerable file. It
rewards over-flagging, so treat those numbers as a floor, not a like-for-like comparison with
CWE-aware runs.

**Are labels hidden in the filenames?**
No. File IDs are shuffled and carry no class or label information. The CSV answer keys are the only
source of labels.

**I scored against 2026.07.22. Is that still valid?**
No. That release is withdrawn. See the README's
[Corrections and ground-truth disputes](README.md#corrections-and-ground-truth-disputes) section.

**I think a label is wrong. How do I report it?**
Open a ground-truth challenge that names the affected case, its published label, and the semantic
basis for disputing it. A published answer key is never silently replaced.

**Which Python do I need for the scorers?**
Python 3; both scorers are tested on Python 3.12. They use only the standard library and have no
dependencies.
