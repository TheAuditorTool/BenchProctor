# BenchProctor

**Ground truth for SAST.** An open benchmark corpus with machine-readable ground truth and a
deterministic SARIF scorer for measuring how accurately a static analysis tool identifies true
vulnerabilities in benchmark code and how often it flags safe code.

**[benchproctor.com](https://benchproctor.com)** · [blog](https://blog.benchproctor.com) · Apache-2.0

> ## Release status
>
> We publish a language only once its labels pass our full gate suite. We won't ship labels we can't defend.
>
> **Release 2026.07.22: 2,938,418 labeled benchmark cases.**
>
> Exactly 1,469,209 are vulnerable and 1,469,209 are safe.
>
> **This release includes all 11 languages** as standalone finding cases:
>
> Java · Python · Go · Rust · TypeScript · JavaScript · PHP · Ruby · Bash · C · C++
>
> The release spans 21 framework targets and three sizes: `quicktest`, `normal`, and `enterprise`.
> Some cases use shared runtime or companion files required by their language or framework;
> these files are not scored separately.
> Cross-file chains, polyglot scenarios, and adversarial evasion cases are in active development,
> tracked in [roadmap.md](roadmap.md).

A SAST tool is only as trustworthy as its measured performance, and measuring that performance
requires ground truth. BenchProctor provides cases labeled `vulnerable` or `safe`, allowing you
to score compatible SARIF 2.1.0 output and calculate its true-positive rate, false-positive rate,
and Youden's J.

## Quick start

```bash
# 1. extract one release bundle
unzip Benchmarks/normal/java/benchproctor-java-normal-2026.07.22.zip -d benchproctor-java-normal

# 2. scan one framework's testcode and export SARIF 2.1.0
your-tool scan ./benchproctor-java-normal/spring/testcode --format sarif -o results.sarif

# 3. score against its answer key (standard-library Python, zero dependencies)
python ./benchproctor-java-normal/score_sarif.py results.sarif \
  ./benchproctor-java-normal/spring/expectedresults-2026.07.22.csv

# 4. read category-averaged and flat-aggregate TPR, FPR, and Youden's J
```

The scorer recovers each finding's CWE from the SARIF `ruleId`, the result/rule `properties` or
`tags` (e.g. `external/cwe/cwe-089`), or CWE `taxa`. This supports many common SARIF encodings
without configuration. If your tool emits no CWE, add `--match-mode filename` (any finding on a
vulnerable file counts; this rewards over-flagging, so prefer the default). The same
`score_sarif.py` ships inside every release bundle.

## Why another benchmark

Many existing public SAST benchmarks exhibit one or more of these structural limitations:

- **Fixed and unchanging cases.** A static set of human-written cases can encourage
  benchmark-specific tuning over time, making results less indicative of generalization to unseen
  code.
- **Labels encoded in filenames.** When a test lives at
  `sqli/Test01729_true_positive.java`, a scanner can score well by matching the path rather than
  analyzing the code.
- **Limited structural coverage.** Many suites focus on one language and single-file findings,
  without testing multi-step propagation or safeguards that are present but ineffective.

BenchProctor reduces exact-case memorization and label leakage by construction, then broadens
coverage across 11 languages and 21 framework targets with safeguard-aware, multi-step cases.
Cross-file chains and polyglot scenarios remain separate future axes tracked on the
[roadmap](roadmap.md).

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
| **Supporting artifacts** | 2,172 companion and shared-runtime files; not scored separately |
| **Shape** | standalone finding cases; some require companion assets or shared runtime files |

| Size | Framework suites | Categories per suite | Sampling per category | Vulnerable | Safe | Total cases |
|---|---:|---:|---:|---:|---:|---:|
| `quicktest` | 21 | 34–62 | 50 vulnerable + 50 safe | 59,100 | 59,100 | 118,200 |
| `normal` | 21 | 124–218 | up to 100 vulnerable + 100 safe | 420,333 | 420,333 | 840,666 |
| `enterprise` | 21 | 124–218 | up to 250 vulnerable + 250 safe | 989,776 | 989,776 | 1,979,552 |
| **Total** | **63** |  |  | **1,469,209** | **1,469,209** | **2,938,418** |

Every size keeps the vulnerable/safe split exactly balanced. Under Youden's J, a flag-everything
tool scores 0 because its true-positive and false-positive rates are both 100%. The release also
contains 2,172 companion or shared-runtime files required by some cases. These files are part of
their suite's code, not additional cases, so they do not receive separate labels.

### How it's built

- **Combinatorial, not hand-written.** Each category models security-relevant behavior using the
  applicable components of four axes: where untrusted input enters (**source**), how it travels
  (**propagator**), what would neutralize it (**sanitizer or safeguard**), and the dangerous
  operation it reaches (**sink**). The generator combines dozens of components across these axes
  for each language. A vulnerable case omits or defeats the relevant safeguard; its safe
  counterpart applies it correctly. Every emitted case is constrained to a valid, analyzable path
  using real language and framework APIs.
- **Synthetic by design.** The corpus intentionally isolates scoring-relevant security properties.
  Individual cases use real APIs but are not intended to represent complete production features.
- **Anti-leakage by construction.** Emitted files carry no comments, no CWE tags, no category names,
  or label-bearing identifiers. File IDs are shuffled, so filenames do not encode a case's category
  or label. The CSV answer key is the only published source of labels.
- **Seed rotation.** Each release uses a fixed seed. Holding the generator, templates, and toolchain
  constant, the same seed reproduces the corpus byte-for-byte. A new seed emits different
  combinations and identifiers while preserving the benchmark's stated scoring invariants: CWE
  identity, difficulty distribution, 50/50 balance, and language/framework coverage. This limits
  the usefulness of exact-file and filename memorization and is designed to support cross-release
  score comparability. Structural generalization across releases remains possible and is expected.

## What makes it hard

Detecting a bare `eval(input)` is only a baseline. The corpus emphasizes cases intended to exercise
dataflow and safeguard reasoning beyond token or pattern matching:

- **Framework-native APIs.** Real request accessors, DTOs and Pydantic models, ORM and driver
  calls; the taint flows through idiomatic code, not toy snippets.
- **Broken-safeguard variants.** A safeguard is present but ineffective: a flawed regex,
  wrong-context escaping, or an insufficient length limit. A scanner that trusts the mere presence
  of a safeguard may mislabel the vulnerable case as safe; the corresponding safe case applies an
  effective safeguard for the specified sink.
- **Multi-step taint.** Taint travels from source to sink through propagators such as decoding,
  collection round-trips, and conditional dispatch that a path-insensitive matcher may miss.

## Languages & frameworks

All 11 languages ship as standalone finding cases, each cleared through the same gate suite:

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
| **Total** |  | **21** | **242 in union** | **2,938,418** |

Quicktest selects 34–62 prevalent categories per framework target. Normal and enterprise use each
language's full applicable set, ranging from 124 to 218 categories. C and C++ include memory-safety
classes such as out-of-bounds read/write, use-after-free, and integer overflow.

## Web-risk category coverage

| Category | Covered CWEs / mapped CWEs | Coverage or scope note |
|---|---|---|
| A01 Broken Access Control | 36 / 40 | 90% |
| A02 Security Misconfiguration | 11 / 16 | 69% |
| A03 Software Supply Chain | 0 / 6 | Out of scope: composition analysis, not code-pattern SAST |
| A04 Cryptographic Failures | 31 / 32 | 97% |
| A05 Injection | 30 / 37 | 81% |
| A06 Insecure Design | 26 / 39 | 67% |
| A07 Authentication Failures | 34 / 36 | 94% |
| A08 Software & Data Integrity | 11 / 14 | 79% |
| A09 Logging & Alerting Failures | 3 / 5 | 60% |
| A10 Exceptional Conditions | 23 / 24 | 96% |

Against this web-risk taxonomy, 205 of 249 mapped CWEs are covered (82.3%). This taxonomy view is
separate from the 231 distinct CWE IDs represented by cases in the release. The uncovered items
are primarily config-level, supply-chain, or runtime-only concerns outside this benchmark's current
static code-pattern scope.

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
| 0% | No measured discrimination: TPR equals FPR; flag-everything and flag-nothing both land here |
| -100% | Inverted: flags safe code, misses real bugs |

Scores are reported in two forms. The **category-averaged** headline score weights each category
equally so large categories cannot dominate; the **flat aggregate** score weights every case
equally. Any tool that emits compatible SARIF 2.1.0 can be scored; the scorer is a single
standard-library Python file with no dependencies.

## How the labels are verified

Before a language is published, every emitted finding case passes a gate suite: it must compile
(or parse), each `vulnerable` case must carry a real source-to-sink taint flow, each `safe` twin
must actually neutralize it for that sink, and the recorded sink line must match the scored sink
operation.

Published bundles contain test code, required support artifacts, CSV answer keys, the scorer,
manifests, checksums, and documentation. Internal per-case proof metadata and the perfect-score
oracle SARIF used for self-verification are deliberately **not** published. The CSV is the sole
published source of labels; test files contain no proof markers or label metadata from which those
labels can be inferred.

## Bundles and integrity

Release 2026.07.22 contains 33 logical language-size bundles: 11 languages × 3 sizes. Six enterprise
bundles exceeded 95 MiB and were split into two parts, producing 39 final ZIP files. The final ZIP
set occupies 1,587,819,973 bytes (1,514.3 MiB).

Each logical bundle is self-contained; when a bundle is distributed as two ZIP files, the complete
pair constitutes the bundle. It contains a `testcode/` directory for each framework, the
`expectedresults-<version>.csv` answer key, the bundled `score_sarif.py`, a
`benchproctor-manifest.json` (version, per-framework counts, and SHA-256 checksums), and a README.
`SHASUMS256.txt` and per-file checksum sidecars let you verify every download.

## Corrections and ground-truth disputes

At this scale, ground-truth defects are possible and must be handled transparently.

A ground-truth challenge should identify the affected case, its published label, and the semantic
basis for disputing that label. Confirmed defects are traced to and corrected in the generator or
template wherever possible, and every affected family is regenerated.

Published release artifacts are immutable. Corrections ship in a new version whose changelog
identifies:

- the affected cases and generator or template families;
- the cause and correction;
- the number and direction of label changes;
- any resulting changes to BenchProctor-published scanner scores.

Released answer keys are never silently replaced.

## Releases

Corpora are versioned and released periodically. The scorer in `scripts/score_sarif.py` uses only
the Python standard library: clone the repository, point the scorer at a corpus and your SARIF, and
read the resulting metrics.

## License

Apache License 2.0, see [LICENSE](LICENSE). Created and maintained by the author of BenchProctor.
