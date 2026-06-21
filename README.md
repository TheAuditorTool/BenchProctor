# BenchProctor

**Ground truth for SAST.** An open, machine-verifiable benchmark corpus for measuring how
accurately a static analysis tool finds real vulnerabilities — and how often it flags safe code.

**[benchproctor.com](https://benchproctor.com)** · [blog](https://blog.benchproctor.com) · Apache-2.0

> ## Release status
>
> We publish a language only once its labels pass our full gate suite — we won't ship labels we can't defend.
>
> - **Java — live now** (Spring, Jakarta EE), standalone.
> - **Python — live now** (Flask, Django, FastAPI), standalone.
> - Go, Rust, TypeScript, JavaScript, PHP, Ruby, and Bash follow as each clears the same bar — see [roadmap.md](roadmap.md).
>
> Each language ships in three sizes — `quicktest`, `normal`, and `enterprise`.

A SAST tool is only as trustworthy as its accuracy, and accuracy is unmeasurable without ground
truth. BenchProctor gives you labeled corpora — programs marked `vulnerable` or `safe` — so you
can score any tool that emits SARIF 2.1.0 and get a real number: true-positive rate,
false-positive rate, and overall detection accuracy (Youden's J).

## Quick start

```bash
# 1. run your scanner against a suite, export SARIF 2.1.0
your-tool scan ./Benchmarks/normal/java/spring --format sarif -o results.sarif

# 2. score against the answer key (standard-library Python, zero dependencies)
python scripts/score_sarif.py results.sarif Benchmarks/normal/java/spring/expectedresults-*.csv

# 3. read TPR, FPR, and your Youden's J — category-averaged and flat aggregate
```

The scorer recovers each finding's CWE from the SARIF `ruleId`, the result/rule `properties` or
`tags` (e.g. `external/cwe/cwe-089`), or CWE `taxa` — so most tools work as-is. If your tool emits no
CWE at all, add `--match-mode filename` (any finding on a vulnerable file counts; this rewards
over-flagging, so prefer the default).

## Why another benchmark

Existing public SAST benchmarks share three structural weaknesses:

- **Hand-authored and frozen.** A fixed set of human-written cases gets published once and never
  changes, so tools — and the models behind them — overfit to it. A high score stops meaning
  real-world accuracy.
- **The filename leaks the answer.** When a test lives at `sqli/Test01729_true_positive.java`, a
  scanner can score well by matching the path, not by analyzing code.
- **One language, one file, no defenses.** Real findings cross files, services, and languages and
  sit next to sanitizers that almost work. Single-file, single-language suites never exercise that.

BenchProctor is built to remove all three.

## What's in the corpus

| | |
|---|---|
| **Live now** | Java (Spring, Jakarta EE) · Python (Flask, Django, FastAPI) — standalone |
| **Vulnerability types** | ~210 CWE-mapped categories supported across Java + Python |
| **Sizes per language** | `quicktest` · `normal` · `enterprise` (see below) |
| **Balance** | 50 / 50 vulnerable / safe, per category |
| **Roadmap** | Go, Rust, TypeScript, JavaScript, PHP, Ruby, Bash — see [roadmap.md](roadmap.md) |

Each language ships in three sizes, so you can trade run time for depth:

- **`quicktest`** (~10k tests/language) — the most prevalent CWEs at 25 vulnerable + 25 safe per type. A fast first read.
- **`normal`** (~40k) — ~all supported CWEs at 50 + 50 per type. The headline scoreable corpus.
- **`enterprise`** (all CWEs, deepest sampling, up to 200 + 200 per type) — for tight confidence intervals.

- **Combinatorial, not hand-written.** Each category is a vulnerability class expressed as a taint
  flow over four axes — where untrusted input enters (**source**), how it travels (**propagator**),
  what would neutralize it (**sanitizer**), and the dangerous call it reaches (**sink**). The corpus
  is assembled by combining those building blocks (42 sources × 40 propagators × 65 sanitizers ×
  58 sinks): a vulnerable case omits an effective sanitizer; its safe twin applies one. Every
  emitted combination is constrained to a realistic flow.
- **Anti-leakage by construction.** Emitted files carry no comments, no CWE tags, no category names,
  and no hints in identifiers. File IDs are shuffled, so a filename reveals nothing about a file's
  category or label. The CSV answer key is the only ground truth.
- **Quarterly rotation.** Each release is generated from a fixed seed that changes *which*
  combinations are emitted — so the actual code differs every quarter — while holding every
  scoring-relevant invariant constant (CWE identity, difficulty distribution, 50/50 balance,
  language/framework coverage). Same seed reproduces the corpus byte-for-byte; a new seed yields
  fresh variants you can't have pre-trained against. Last quarter's score stays comparable.

## What makes it hard

Detecting a bare `eval(input)` is table stakes. Every category is weighted toward the cases that
separate a real analyzer from a pattern matcher:

- **Realistic framework code.** Real request accessors, DTOs / Pydantic models, ORM and driver
  calls — the taint flows through idiomatic code, not toy snippets.
- **Broken-sanitizer variants.** A sanitizer is present but bypassed — a flawed regex, wrong-context
  escaping, an insufficient length limit. A scanner that trusts the mere presence of a sanitizer
  mislabels these as vulnerable's safe twin; the effective twin is genuinely safe.
- **Multi-step taint.** Source to sink through propagators — decoding, collection round-trips,
  conditional dispatch — that a path-insensitive matcher loses.

Cross-file CWE chains, polyglot microservice scenarios, and adversarial / SAST-evasion cases are on
the [roadmap](roadmap.md); this release is single-file standalone.

## Languages & frameworks

**Live now (standalone):**

| Language | Frameworks |
|---|---|
| Java | Spring, Jakarta EE |
| Python | Flask, Django, FastAPI |

**On the roadmap** (each ships when it clears the same gates): Go (net/http, Gin) · Rust
(Actix-web, Axum) · TypeScript (NestJS, Express) · JavaScript (Express, Koa) · PHP (Laravel,
Symfony) · Ruby (Rails, Sinatra) · Bash. Adding a language changes nothing about the categories, so
coverage stays uniform across the matrix.

## Web-risk category coverage

| Category | Covered / Mapped | |
|---|---|---|
| A01 Broken Access Control | 37 / 40 | 92% |
| A02 Security Misconfiguration | 11 / 16 | 69% |
| A03 Software Supply Chain | 0 / 6 | composition analysis, not code-pattern SAST |
| A04 Cryptographic Failures | 30 / 32 | 94% |
| A05 Injection | 31 / 37 | 83% |
| A06 Insecure Design | 27 / 39 | 69% |
| A07 Authentication Failures | 34 / 36 | 94% |
| A08 Software & Data Integrity | 8 / 14 | 57% |
| A09 Logging & Alerting Failures | 5 / 5 | 100% |
| A10 Exceptional Conditions | 22 / 24 | 92% |

213 of 249 mapped CWEs (85.5%). The remainder is config-level, supply-chain, or runtime-only — not
expressible as a static code pattern.

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
| +100% | Perfect — catches everything, zero false alarms |
| 0% | No better than guessing (where a flag-everything tool lands on a 50/50 corpus) |
| -100% | Inverted — flags safe code, misses real bugs |

Scores are reported two ways: **category-averaged** (each category weighted equally so large
categories can't dominate — the headline number) and **flat aggregate**. Any tool that emits SARIF
2.1.0 can be scored; the scorer is a single standard-library Python file with no dependencies.

## How the labels are verified

Before a language is published, every emitted file passes a gate suite: it must compile (or parse),
each `vulnerable` case must carry a real source-to-sink taint flow, each `safe` twin must actually
neutralize it for that sink, and the recorded sink line must be the line the vulnerability lives on.
What ships here is the testcode plus the CSV answer key — nothing more. The per-file proof metadata
and the perfect-score oracle SARIF we use to self-verify are deliberately **not** published, so the
answer key can't be reconstructed from a shipped file.

## Releases

Corpora are versioned and released quarterly. The scorer in `scripts/score_sarif.py` is
standard-library Python only — clone, point it at a corpus and your SARIF, and read your number.

## License

Apache License 2.0 — see [LICENSE](LICENSE). Created and maintained by the author of BenchProctor.
