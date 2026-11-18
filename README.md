# BenchProctor

**Ground truth for SAST.** An open benchmark with machine-readable ground truth and deterministic
SARIF scorers, for measuring how accurately a static analysis tool identifies true vulnerabilities
in benchmark code and how often it flags safe code.

**[benchproctor.com](https://benchproctor.com)** · [blog](https://blog.benchproctor.com) · Apache-2.0

> ## Release status
>
> **Release 2026.11.19 is the current release.** It is a curated release:
>
> - **14,280 standalone cases** in 11 languages across 21 framework targets, exactly 7,140
>   vulnerable and 7,140 safe;
> - **368 multi-service applications** in five languages, holding 5,299 labeled flows.
>
> It is published as plain files in `Benchmarks/`, so every case and answer key can be read here
> without unpacking anything. Earlier releases are kept under [`archive/`](archive/).
>
> Releases are curated. Each release is a fresh draw: easy and medium difficulty only, on a fixed
> list of frameworks and weakness classes. The larger corpus it is
> drawn from is not published. See [What this release does not contain](#what-this-release-does-not-contain).
>
> **Release 2026.07.22 is withdrawn.** An audit found label and realism defects in families it
> was built from. Do not report scores against it. See
> [Corrections and ground-truth disputes](#corrections-and-ground-truth-disputes).

A SAST tool is only as trustworthy as its measured performance, and measuring that performance
requires ground truth. BenchProctor provides cases labeled `vulnerable` or `safe`, so you can score
compatible SARIF 2.1.0 output and calculate its true-positive rate, false-positive rate, and
Youden's J.

## Quick start

```bash
# 1. clone this repository; the current release is in Benchmarks/

# 2. scan one framework's testcode and export SARIF 2.1.0
your-tool scan Benchmarks/standalone/java/spring/testcode --format sarif -o results.sarif

# 3. score against its answer key (standard-library Python, zero dependencies)
python Benchmarks/standalone/java/score_sarif.py results.sarif \
  Benchmarks/standalone/java/spring/expectedresults-2026.11.19.csv

# 4. read category-averaged and flat-aggregate TPR, FPR, and Youden's J
```

The scorer recovers each finding's CWE from the SARIF `ruleId`, the result or rule `properties` or
`tags` (for example `external/cwe/cwe-089`), or CWE `taxa`. This supports many common SARIF
encodings without configuration. If your tool emits no CWE, add `--match-mode filename` (any
finding on a vulnerable file counts; this rewards over-flagging, so prefer the default). The same
`score_sarif.py` ships in every standalone language folder. The applications have their own scorer; see
[Applications](#applications).

## Why another benchmark

Many existing public SAST benchmarks exhibit one or more of these structural limitations:

- **Fixed and unchanging cases.** A static set of human-written cases can encourage
  benchmark-specific tuning over time, making results less indicative of generalization to unseen
  code.
- **Labels encoded in filenames.** When a test lives at
  `sqli/Test01729_true_positive.java`, a scanner can score well by matching the path rather than
  analyzing the code.
- **Limited structural coverage.** Many suites focus on one language and single-file findings,
  without testing a flow that crosses a service boundary.

BenchProctor reduces exact-case memorization and label leakage by construction, covers 11
languages, and adds multi-service applications whose flows cross a process boundary.

## What's in this release

| | |
|---|---|
| **Release** | `2026.11.19` |
| **Standalone cases** | 14,280: 7,140 vulnerable and 7,140 safe |
| **Languages** | 11: Java, Python, Go, Rust, TypeScript, JavaScript, PHP, Ruby, Bash, C, C++ |
| **Framework targets** | 21 (see the table below) |
| **Weakness classes** | 22, mapped to 22 distinct CWE IDs |
| **Sampling** | 20 vulnerable + 20 safe cases for every framework and class pair: 357 pairs |
| **Applications** | 368 two-service applications over 6 service graphs, in TypeScript, JavaScript, Python, Java and C++ |
| **Application flows** | 5,299 labeled flows: 1,473 vulnerable and 3,826 safe |
| **Difficulty** | easy and medium |

Every framework and class pair is balanced exactly. Under Youden's J, a flag-everything tool
scores 0 because its true-positive and false-positive rates are both 100%. Some cases use shared
runtime or companion files required by their language or framework; these files are not scored
separately.

### What this release does not contain

This is a curated release, and it is deliberately narrow. It does not contain:

- **Cases built around an ineffective safeguard.** In this release a vulnerable case has no
  safeguard, and a safe case has one that works. A tool that treats the presence of any safeguard
  as proof of safety is not penalized here.
- **The deepest propagation patterns.** Flows use direct and medium-depth propagation only.
- **Frameworks, weakness classes and application shapes beyond the lists on this page.**

Read a score on this release as a floor check on broadly known classes, not as a full assessment.

### How it's built

- **Combinatorial, not hand-written.** Each class models security-relevant behavior using the
  applicable components of four axes: where untrusted input enters (**source**), how it travels
  (**propagator**), what would neutralize it (**sanitizer or safeguard**), and the dangerous
  operation it reaches (**sink**). A vulnerable case omits the safeguard; its safe counterpart
  applies an effective one. Every emitted case is constrained to a valid, analyzable path using
  real language and framework APIs.
- **Synthetic by design.** The corpus intentionally isolates scoring-relevant security properties.
  Individual cases use real APIs but are not intended to represent complete production features.
- **Anti-leakage by construction.** Emitted files carry no comments, no CWE tags, no category names,
  or label-bearing identifiers. File IDs are shuffled, so filenames do not encode a case's class
  or label. The CSV answer keys are the only published source of labels.
- **Seed rotation.** Each release is drawn with its own seed. A new release keeps the same
  languages, frameworks, classes and difficulty, and emits different combinations and
  identifiers. This limits the usefulness of exact-file and filename memorization and is designed
  to support cross-release score comparability. Structural generalization across releases remains
  possible and is expected.

## Languages & frameworks

| Language | Framework targets | Targets | Classes per target | Cases |
|---|---|---:|---:|---:|
| Java | Spring, Jakarta EE | 2 | 18 | 1,440 |
| Python | Flask, Django, FastAPI | 3 | 18 | 2,160 |
| Go | Gin, net/http | 2 | 15 | 1,200 |
| Rust | Actix-web, Axum | 2 | 15 | 1,200 |
| TypeScript | NestJS, Express | 2 | 18 | 1,440 |
| JavaScript | Express, Koa | 2 | 18 | 1,440 |
| PHP | Laravel, Symfony | 2 | 18 | 1,440 |
| Ruby | Rails, Sinatra | 2 | 17 | 1,360 |
| C++ | cpp-httplib, standalone | 2 | 19 | 1,520 |
| C | standalone | 1 | 16 | 640 |
| Bash | standalone | 1 | 11 | 440 |
| **Total** |  | **21** | **22 in union** | **14,280** |

A framework target carries the classes that occur in its language. C and C++ include memory-safety
classes; the managed languages do not.

### C and C++ prerequisites

"Standalone" means one file per case, not free of dependencies. The C and C++ standard libraries
have no SQL, HTTP, cryptography or message-queue API, so some cases call a library: 142 of the 640
C cases call SQLite, libcurl or OpenSSL, and 17 of the 1,520 C++ cases call the hiredis or
RabbitMQ C client. A tool that compiles the cases, or resolves their `#include` lines, needs those
libraries' development headers:

- Fedora / RHEL: `dnf install openssl-devel sqlite-devel libcurl-devel hiredis-devel librabbitmq-devel`
- Debian / Ubuntu: `apt install libssl-dev libsqlite3-dev libcurl4-openssl-dev libhiredis-dev librabbitmq-dev`

Each standalone language folder's README and `benchproctor-manifest.json` list exactly which
libraries its cases include. No label depends on a header version.

## Weakness classes

| Class | CWE | Class | CWE |
|---|---|---|---|
| SQL injection | CWE-89 | Server-side request forgery | CWE-918 |
| OS command injection | CWE-78 | Code injection | CWE-94 |
| Path traversal | CWE-22 | Deserialization of untrusted data | CWE-502 |
| Cross-site scripting | CWE-79 | XML external entity | CWE-611 |
| LDAP injection | CWE-90 | Open redirect | CWE-601 |
| XPath injection | CWE-643 | Integer overflow | CWE-190 |
| Weak cipher | CWE-327 | NULL pointer dereference | CWE-476 |
| Weak hash | CWE-328 | Stack-based buffer overflow | CWE-121 |
| Weak random | CWE-330 | Heap-based buffer overflow | CWE-122 |
| Cookie without the secure attribute | CWE-614 | Buffer over-read | CWE-126 |
| Trust boundary violation | CWE-501 | Use after free | CWE-416 |

## Applications

An application is a small project made of two services that call each other over HTTP, each with
its own container file. One primary flow starts at the entry service and ends at a sink in the
backend service. Further single-file flows, vulnerable and safe, and plain safe modules sit
around it, all of them labeled, so a tool has to tell the flows that matter from the code that
surrounds them. Each application also carries a `docker-compose.yml`.

| Service graph | Applications | Flows | Vulnerable | Safe |
|---|---:|---:|---:|---:|
| Express (TypeScript) to Flask | 64 | 920 | 255 | 665 |
| NestJS to Spring | 64 | 920 | 255 | 665 |
| Express (JavaScript) to Django | 64 | 923 | 258 | 665 |
| Express (TypeScript) to cpp-httplib | 48 | 694 | 194 | 500 |
| FastAPI to Spring | 64 | 921 | 255 | 666 |
| Jakarta EE to NestJS | 64 | 921 | 256 | 665 |
| **Total** | **368** | **5,299** | **1,473** | **3,826** |

Applications are built around six classes (SQL injection, cross-site scripting, OS command
injection, server-side request forgery, path traversal, deserialization) and two two-stage chains
(an unauthenticated entry leading to cross-site scripting, and an unvalidated URL leading to
server-side request forgery). The C++ graph carries six of the eight: it has no deserialization
application and no unvalidated-URL chain. In half of the applications the chain completes; in the
other half a control on the path holds.

```bash
your-tool scan Benchmarks/applications/nestjs-spring/applications --format sarif -o results.sarif
python Benchmarks/applications/score_apps.py \
  --flows  Benchmarks/applications/nestjs-spring/expectedresults-2026.11.19.csv \
  --chains Benchmarks/applications/nestjs-spring/expectedresults-chains-2026.11.19.csv \
  --tool-sarif results.sarif
```

`score_apps.py` reports three numbers side by side and never averages them: whether each flow was
judged correctly (Youden's J), whether the right CWE was named for the flows judged correctly, and
how much of the service graph the tool reconstructed.

## Scoring

Every standalone case carries a ground-truth label (`vulnerable` or `safe`) in a CSV answer key.
After a tool runs, scoring computes a confusion matrix and one subtraction:

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

Scores are reported in two forms. The **category-averaged** headline score weights each class
equally so large classes cannot dominate; the **flat aggregate** score weights every case equally.
With twenty cases per side, one case moves a single framework and class pair by five points and a
framework's headline score by well under one point, so per-class scores carry real signal. Any tool that emits compatible
SARIF 2.1.0 can be scored; both scorers are single standard-library Python files with no
dependencies.

## How the labels are verified

Before release, every source file in this release was put through the native toolchain for its
language. Nothing was sampled:

- **Java:** every standalone file compiled with `javac`, one run per framework; every Java service
  of the applications compiled with Maven.
- **Python:** every standalone file parsed, and every case checked for undefined names; every
  Python service of the applications byte-compiled.
- **Go:** `go build` and `go vet` over each framework's module.
- **Rust:** `cargo check` over each framework's crate.
- **TypeScript:** `tsc` in strict mode over every TypeScript source file, standalone and
  applications.
- **C++ applications:** every C++ service built with its own `Makefile`.
- **JavaScript, PHP, Ruby, C, C++, Bash:** every file syntax-checked with `node --check`, `php -l`,
  `ruby -c`, `gcc`, `g++` and `bash -n`. The C and C++ files were checked with their libraries'
  development headers installed (see [C and C++ prerequisites](#c-and-c-prerequisites)).

On top of that, a suite of deterministic gates runs with no AI and no LLM-as-judge: each
`vulnerable` case must carry a real source-to-sink flow, each `safe` twin must neutralize it for
that sink, the recorded sink line must match the scored operation, and dozens of further structural
and idiom checks must hold. For the applications, further gates check that each service graph
matches the services on disk and that every vulnerable flow's scored line holds a statement.

Finally, every bundle was scored the way you would score it, with the scorer shipped in it and the
answer keys shipped beside the code, against a perfect answer: every standalone
framework scores +100%, and on every application graph every flow is judged right, every CWE is
named and every service-graph edge is recovered.

The applications were also run. One application of every archetype was built and brought up
under Docker, a request was sent to its entry service, and the sink's own log confirmed the
payload arrived.

Published bundles contain test code, required support artifacts, CSV answer keys, the scorers,
manifests, checksums, and documentation. Internal per-case proof metadata and the perfect-score
oracle SARIF used for self-verification are deliberately **not** published. The CSVs are the sole
published source of labels; test files contain no proof markers or label metadata from which those
labels can be inferred.

## Layout and integrity

Release 2026.11.19 is published as plain files under `Benchmarks/`: one folder per language under
`Benchmarks/standalone/` and one for the applications under `Benchmarks/applications/`, 25,721
files in all (45.6 MiB). `Benchmarks/SHASUMS256.txt` lists the SHA-256 of every file; from
`Benchmarks/`, `sha256sum -c SHASUMS256.txt` checks them all.

Each standalone language folder holds a `testcode/` directory for each framework, the
`expectedresults-<version>.csv` answer key, the bundled `score_sarif.py`, a
`benchproctor-manifest.json` (version, per-framework counts, SHA-256 checksums of the answer key
and the scorer, and the libraries the C and C++ cases include), and a README. The applications
folder holds one directory per service graph with its `applications/`, its two answer-key CSVs,
and `score_apps.py`.

Earlier releases are kept whole under [`archive/`](archive/), one folder per release, each with
its own `SHASUMS256.txt`. Release 2026.11.16 was published as one zip per bundle; it is kept there
unpacked, and its original zips remain in this repository's history.

## Corrections and ground-truth disputes

Ground-truth defects are possible and must be handled in the open.

A ground-truth challenge should identify the affected case, its published label, and the semantic
basis for disputing that label. Confirmed defects are traced to and corrected in the generator or
template wherever possible, and every affected family is regenerated.

A published release is never silently replaced. A correction ships as a new release whose
changelog identifies the affected families, the cause and the correction, and the direction of any
label change.

### Withdrawal of release 2026.07.22

Release 2026.07.22 (2,938,418 cases) is withdrawn as a whole, and its bundles are no longer
distributed: they were removed from this repository together with its history. An audit before this
release found the following in families it was built from:

- **A wrong `safe` label on 314 cases.** Some safe SQL injection cases guarded the value with a
  character allowlist and then placed it unquoted in the statement. An allowlist of identifier
  characters does not protect an unquoted value: the input `id` turns `WHERE id = id` into a
  condition that matches every row. A scan of every file in the withdrawn bundles found 314 such
  cases, all in the SQL injection class: 116 in Java and 198 in Python, and none in the other
  nine languages. By size: `quicktest` 58, `normal` 87, `enterprise` 169. Direction of the
  change: `safe` cases that should have been `vulnerable`. The value is now quoted.
- **Safe cases whose dangerous line could never run.** A value was wrapped in fixed text and then
  checked as a whole, so the check rejected every input. The label was right and the case tested
  nothing. This release leaves those propagation forms out.
- **Entry points that cannot occur.** Some request handlers in Java, Rust and Ruby read
  command-line input. No label was wrong, but the flow could not happen in a deployed service.
- **Unidiomatic Java.** Unused imports, a persistence factory built on every request, and
  repository types declared inside a handler. No label was affected.

Only the first item changed a label. Scores reported against 2026.07.22 should not be compared
with scores on any later release.

## Releases

Release 2026.11.19 is the current release, in `Benchmarks/`; earlier releases are under
[`archive/`](archive/). The scorers in `scripts/` use only the Python standard library: clone the repository, point a scorer at a corpus and your SARIF, and read the resulting
metrics. The release history is in [changelog.md](changelog.md), and a step-by-step guide is in
[usage.md](usage.md).

## License

Apache License 2.0, see [LICENSE](LICENSE). Created and maintained by the author of BenchProctor.
