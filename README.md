# BenchProctor

**Ground truth for SAST.** An open, machine-verifiable benchmark corpus for measuring how
accurately a static analysis tool finds real vulnerabilities, and how often it flags safe code.

**[benchproctor.com](https://benchproctor.com)** · [blog](https://blog.benchproctor.com) · Apache-2.0

> ## Release status
>
> We publish a language only once its labels pass our full gate suite. We won't ship labels we can't defend.
>
> **Release 2026.07.22: 2,938,418 independently labeled benchmark cases.**
>
> Exactly 1,469,209 are vulnerable and 1,469,209 are safe.
>
> **All 11 languages are live now**, standalone:
>
> Java · Python · Go · Rust · TypeScript · JavaScript · PHP · Ruby · Bash · C · C++
>
> across 21 framework targets and three sizes: `quicktest`, `normal`, and `enterprise`.
> Cross-file chains, polyglot scenarios, and adversarial evasion cases are in active development,
> tracked in [roadmap.md](roadmap.md).

A SAST tool is only as trustworthy as its accuracy, and accuracy is unmeasurable without ground
truth. BenchProctor gives you labeled corpora (programs marked `vulnerable` or `safe`) so you
can score any tool that emits SARIF 2.1.0 and get a real number: true-positive rate,
false-positive rate, and overall detection accuracy (Youden's J).

## Quick start

```bash
# 1. extract one release bundle
unzip Benchmarks/normal/java/benchproctor-java-normal-2026.07.22.zip -d benchproctor-java-normal

# 2. scan one framework's testcode and export SARIF 2.1.0
your-tool scan ./benchproctor-java-normal/spring/testcode --format sarif -o results.sarif

# 3. score against its answer key (standard-library Python, zero dependencies)
python ./benchproctor-java-normal/score_sarif.py results.sarif \
  ./benchproctor-java-normal/spring/expectedresults-2026.07.22.csv

# 4. read TPR, FPR, and your Youden's J, category-averaged and flat aggregate
```

The scorer recovers each finding's CWE from the SARIF `ruleId`, the result/rule `properties` or
`tags` (e.g. `external/cwe/cwe-089`), or CWE `taxa`, so most tools work as-is. If your tool emits no
CWE at all, add `--match-mode filename` (any finding on a vulnerable file counts; this rewards
over-flagging, so prefer the default). The same `score_sarif.py` ships inside every release bundle.

## Why another benchmark

Existing public SAST benchmarks share three structural weaknesses:

- **Hand-authored and frozen.** A fixed set of human-written cases gets published once and never
  changes, so tools, and the models behind them, overfit to it. A high score stops meaning
  real-world accuracy.
- **The filename leaks the answer.** When a test lives at `sqli/Test01729_true_positive.java`, a
  scanner can score well by matching the path, not by analyzing code.
- **One language, one file, no defenses.** Real findings cross files, services, and languages and
  sit next to sanitizers that almost work. Single-file, single-language suites never exercise that.

BenchProctor removes frozen-case and label-leakage effects by construction, then broadens coverage
across 11 languages and 21 framework targets with sanitizer-aware, multi-step cases. Cross-file
chains and polyglot scenarios are tracked separately on the [roadmap](roadmap.md).

## What's in the corpus

| | |
|---|---|
| **Release** | `2026.07.22` |
| **Languages** | 11: Java, Python, Go, Rust, TypeScript, JavaScript, PHP, Ruby, Bash, C, C++ |
| **Framework targets** | 21 (see the table below) |
| **Vulnerability coverage** | 242 emitted categories mapped to 231 distinct CWE IDs |
| **Sizes** | 3 per language: `quicktest` · `normal` · `enterprise` |
| **Framework-size suites** | 63: 21 framework targets × 3 sizes |
| **Labeled benchmark cases** | 2,938,418 |
| **Vulnerable / safe** | 1,469,209 / 1,469,209 |
| **Balance** | exactly 50 / 50 |
| **Supporting artifacts** | 2,172 companion and shared-runtime files; not independent scoring cases |
| **Shape** | standalone cases; some use companion assets or shared runtime files |

| Size | Framework suites | Categories per suite | Sampling per category | Vulnerable | Safe | Total cases |
|---|---:|---:|---:|---:|---:|---:|
| `quicktest` | 21 | 34–62 | 50 vulnerable + 50 safe | 59,100 | 59,100 | 118,200 |
| `normal` | 21 | 124–218 | up to 100 vulnerable + 100 safe | 420,333 | 420,333 | 840,666 |
| `enterprise` | 21 | 124–218 | up to 250 vulnerable + 250 safe | 989,776 | 989,776 | 1,979,552 |
| **Total** | **63** |  |  | **1,469,209** | **1,469,209** | **2,938,418** |

Every size keeps the vulnerable/safe split exactly balanced, so a flag-everything tool scores 0.
The release also contains 2,172 companion or shared-runtime files required by some cases. These
files are part of their suite's code, not additional cases, so they do not receive separate labels.

### How it's built

- **Combinatorial, not hand-written.** Each category is a vulnerability class expressed as a taint
  flow over four axes: where untrusted input enters (**source**), how it travels (**propagator**),
  what would neutralize it (**sanitizer**), and the dangerous call it reaches (**sink**). The corpus
  is assembled by combining a library of dozens of each per language: a vulnerable case omits an
  effective sanitizer; its safe twin applies one. Every emitted combination is constrained to a
  realistic flow.
- **Anti-leakage by construction.** Emitted files carry no comments, no CWE tags, no category names,
  and no hints in identifiers. File IDs are shuffled, so a filename reveals nothing about a file's
  category or label. The CSV answer key is the only ground truth.
- **Seed rotation.** Each release is generated from a fixed seed that changes *which* combinations
  are emitted, so the actual code differs every release, while holding every scoring-relevant
  invariant constant (CWE identity, difficulty distribution, 50/50 balance, language/framework
  coverage). Same seed reproduces the corpus byte-for-byte; a new seed yields fresh variants you
  can't have pre-trained against, and last release's score stays comparable.

## What makes it hard

Detecting a bare `eval(input)` is table stakes. Every category is weighted toward the cases that
separate a real analyzer from a pattern matcher:

- **Realistic framework code.** Real request accessors, DTOs / Pydantic models, ORM and driver
  calls; the taint flows through idiomatic code, not toy snippets.
- **Broken-sanitizer variants.** A sanitizer is present but bypassed: a flawed regex, wrong-context
  escaping, an insufficient length limit. A scanner that trusts the mere presence of a sanitizer
  mislabels these as the safe twin; the effective twin is genuinely safe.
- **Multi-step taint.** Source to sink through propagators (decoding, collection round-trips,
  conditional dispatch) that a path-insensitive matcher loses.

## Languages & frameworks

All 11 languages ship standalone, each cleared through the same gate suite:

| Language | Framework targets | Targets | Normal / enterprise categories | Labeled cases |
|---|---|---:|---:|---:|
| Java | Spring, Jakarta EE | 2 | 218 | 307,556 |
| Python | Flask, Django, FastAPI | 3 | 212 | 447,132 |
| Go | Gin, net/http | 2 | 205 | 284,096 |
| Rust | Actix-web, Axum | 2 | 203 | 282,448 |
| TypeScript | NestJS, Express | 2 | 216 | 304,696 |
| JavaScript | Express, Koa | 2 | 216 | 304,696 |
| PHP | Laravel, Symfony | 2 | 212 | 299,156 |
| Ruby | Rails, Sinatra | 2 | 209 | 295,016 |
| C++ | cpp-httplib, standalone | 2 | 182 | 247,512 |
| C | standalone | 1 | 124 | 49,520 |
| Bash | standalone | 1 | 172 | 116,590 |
| **Total** |  | **21** | **242 distinct** | **2,938,418** |

Quicktest selects 34–62 prevalent categories per framework target. Normal and enterprise use each
language's full applicable set, ranging from 124 to 218 categories. C and C++ include memory-safety
classes such as out-of-bounds read/write, use-after-free, and integer overflow.

## Web-risk category coverage

| Category | Covered / Mapped | |
|---|---|---|
| A01 Broken Access Control | 36 / 40 | 90% |
| A02 Security Misconfiguration | 11 / 16 | 69% |
| A03 Software Supply Chain | 0 / 6 | composition analysis, not code-pattern SAST |
| A04 Cryptographic Failures | 31 / 32 | 97% |
| A05 Injection | 30 / 37 | 81% |
| A06 Insecure Design | 26 / 39 | 67% |
| A07 Authentication Failures | 34 / 36 | 94% |
| A08 Software & Data Integrity | 11 / 14 | 79% |
| A09 Logging & Alerting Failures | 3 / 5 | 60% |
| A10 Exceptional Conditions | 23 / 24 | 96% |

Against this web-risk taxonomy, 205 of 249 mapped CWEs are covered (82.3%). This taxonomy view is
separate from the 231 distinct CWE IDs represented by cases in the release. The remainder is
config-level, supply-chain, or runtime-only, not expressible as a static code pattern.

## Scoring

Every test case carries a ground-truth label (`vulnerable` or `safe`) in a CSV answer key. After a
tool runs, scoring computes a confusion matrix and one subtraction:

```
                detected   ignored
 vulnerable        TP         FN
 safe              FP         TN

 TPR  = TP / (TP + FN)     detection rate
 FPR  = FP / (FP + TN)     false-alarm rate
 J    = TPR - FPR          Youden's J  (the score)
```

| Score | Meaning |
|------:|---------|
| +100% | Perfect: catches everything, zero false alarms |
| 0% | No better than guessing (where a flag-everything tool lands on a 50/50 corpus) |
| -100% | Inverted: flags safe code, misses real bugs |

Scores are reported two ways: **category-averaged** (each category weighted equally so large
categories can't dominate, the headline number) and **flat aggregate**. Any tool that emits SARIF
2.1.0 can be scored; the scorer is a single standard-library Python file with no dependencies.

## How the labels are verified

Before a language is published, every emitted file passes a gate suite: it must compile (or parse),
each `vulnerable` case must carry a real source-to-sink taint flow, each `safe` twin must actually
neutralize it for that sink, and the recorded sink line must be the line the vulnerability lives on.
What ships here is the testcode plus the CSV answer key, nothing more. The per-file proof metadata
and the perfect-score oracle SARIF we use to self-verify are deliberately **not** published, so the
answer key can't be reconstructed from a shipped file.

## Bundles and integrity

Release 2026.07.22 contains 33 logical language-size bundles: 11 languages × 3 sizes. Six enterprise
bundles exceeded 95 MiB and were split into two parts, producing 39 final ZIP files. The final ZIP
set occupies 1,587,819,973 bytes (1,514.3 MiB).

Each logical bundle—or the complete pair when split—is self-contained: the `testcode/` per
framework, the `expectedresults-<version>.csv` answer key, the bundled `score_sarif.py`, a
`benchproctor-manifest.json` (version, per-framework counts, SHA-256 checksums), and a README.
`SHASUMS256.txt` and per-file checksum sidecars let you verify every download.

## Releases

Corpora are versioned and released periodically. The scorer in `scripts/score_sarif.py` is
standard-library Python only: clone, point it at a corpus and your SARIF, and read your number.

## License

Apache License 2.0, see [LICENSE](LICENSE). Created and maintained by the author of BenchProctor.
