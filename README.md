# BenchProctor

**Ground truth for SAST.** An open benchmark corpus with machine-readable ground truth and
deterministic scorers for measuring how accurately a static analysis tool identifies true
vulnerabilities and how often it flags safe code. The corpus now spans two shapes: single-file
**standalone** finding cases, and deployable **application** projects that carry taint across
files, languages, and processes.

**[benchproctor.com](https://benchproctor.com)** · [blog](https://blog.benchproctor.com) · Apache-2.0

> ## Release status
>
> We publish a language only once its labels pass our full gate suite. We won't ship labels we can't defend.
>
> **Next release (documented here as v2.0), date-versioned `YYYY.MM.DD` as before.**
>
> This is the largest change since the first release. It ships two shapes together:
>
> - **Standalone**, the single-file finding corpus, rebuilt on a far larger and fully unlocked
>   framework surface: `[PENDING]` labeled cases, split exactly 50 / 50 vulnerable and safe.
> - **Application**, a new shape: small, realistic, buildable polyglot projects, each carrying
>   several planted weaknesses and, where the archetype allows, a compound chain that escalates
>   across services.
>
> **Languages:** 11 general-purpose (Java, Python, Go, Rust, TypeScript, JavaScript, PHP, Ruby,
> Bash, C, C++) plus a Solidity contract emitter.
>
> The corpus draws from a frozen surface of **85 requestable framework lanes** (64 code-language
> lanes and 21 infrastructure substrates) and **118 pinnable libraries**. JavaScript and TypeScript
> are no longer locked to a single framework each; both now draw from the full modern Node surface.
>
> Counts shown as `[PENDING]` are finalized in a second pass once the release completes its
> acceptance gates. The frozen-surface counts (languages, lanes, substrates, libraries) are final.

A SAST tool is only as trustworthy as its measured performance, and measuring that performance
requires ground truth. BenchProctor provides cases labeled `vulnerable` or `safe`, lets you score
compatible SARIF 2.1.0 output, and reports a tool's true-positive rate, false-positive rate, and
Youden's J for standalone, plus a three-part score for the application shape.

## Quick start

For the full walkthrough (choosing a bundle, reading scorer output, and an FAQ) see
[usage.md](usage.md). The essentials:

### Standalone

```bash
# 1. extract one release bundle
unzip Benchmarks/normal/java/benchproctor-java-normal-<version>.zip -d benchproctor-java-normal

# 2. scan one framework's testcode and export SARIF 2.1.0
your-tool scan ./benchproctor-java-normal/spring/testcode --format sarif -o results.sarif

# 3. score against its answer key (standard-library Python, zero dependencies)
python ./benchproctor-java-normal/score_sarif.py results.sarif \
  ./benchproctor-java-normal/spring/expectedresults-<version>.csv

# 4. read category-averaged and flat-aggregate TPR, FPR, and Youden's J
```

The scorer recovers each finding's CWE from the SARIF `ruleId`, the result/rule `properties` or
`tags` (e.g. `external/cwe/cwe-089`), or CWE `taxa`. This supports many common SARIF encodings
without configuration. If your tool emits no CWE, add `--match-mode filename` (any finding on a
vulnerable file counts; this rewards over-flagging, so prefer the default). The same
`score_sarif.py` ships inside every standalone bundle.

### Application

```bash
# 1. extract one application suite bundle
unzip Benchmarks/application/python/django/benchproctor-apps-python-django-<version>.zip -d apps

# 2. scan the whole application tree and export SARIF 2.1.0 (emit codeFlow for chain credit)
your-tool scan ./apps/applications --format sarif -o results.sarif

# 3. score against the two published answer keys with the bundled scorer
python ./apps/score_apps.py \
  --flows  ./apps/expectedresults-<version>.csv \
  --chains ./apps/expectedresults-chains-<version>.csv \
  --tool-sarif results.sarif

# 4. read the triple (J1, A2, S3): flow judgment, CWE identification, chain reconstruction
```

The application scorer reads only the two published CSV files. It reports the three layers side by
side and never averages them into one number, because a single figure would hide which of the three
a tool is weak at.

## Why another benchmark

Many existing public SAST benchmarks exhibit one or more of these structural limitations:

- **Fixed and unchanging cases.** A static set of human-written cases can encourage
  benchmark-specific tuning over time, making results less indicative of generalization to unseen
  code.
- **Labels encoded in filenames.** When a test lives at
  `sqli/Test01729_true_positive.java`, a scanner can score well by matching the path rather than
  analyzing the code.
- **Limited structural coverage.** Many suites focus on one language and single-file findings,
  without testing multi-step propagation, safeguards that are present but ineffective, or taint that
  crosses a service boundary.

BenchProctor reduces exact-case memorization and label leakage by construction, broadens coverage
across 11 languages and a large framework surface with safeguard-aware, multi-step cases, and adds
the application shape so cross-file, cross-language, and cross-process findings become directly
measurable.

## What's in the corpus

| | |
|---|---|
| **Release** | `[PENDING]` (date-versioned `YYYY.MM.DD`; documented as v2.0) |
| **Languages** | 11 general-purpose plus a Solidity contract emitter |
| **Requestable framework lanes** | 85 (64 code-language lanes + 21 infrastructure substrates) |
| **Pinnable libraries** | 118 real third-party libraries the corpus draws on |
| **Shapes** | 2 published: standalone finding cases, application projects |
| **Vulnerability coverage** | `[PENDING]` emitted categories mapped to `[PENDING]` distinct CWE IDs |
| **Standalone sizes** | 3 per language: `quicktest` · `normal` · `enterprise` |
| **Labeled standalone cases** | `[PENDING]` |
| **Vulnerable / safe** | exactly balanced 50 / 50 |
| **Application archetypes** | `[PENDING]` domains across 2-3 tier languages plus 1-2 infra targets |

Every size keeps the vulnerable/safe split exactly balanced. Under Youden's J, a flag-everything
tool scores 0 because its true-positive and false-positive rates are both 100%.

### Standalone sizes

| Size | Sampling per category | Selection |
|---|---|---|
| `quicktest` | 50 vulnerable + 50 safe | the most prevalent classes (CWE Top 25 2024 + OWASP Top 10 2021) |
| `normal` | up to 100 vulnerable + 100 safe | each language's full applicable category set; the headline scoreable corpus |
| `enterprise` | up to 250 vulnerable + 250 safe | full category set at the deepest sampling |

Per-case counts per size are finalized in the second pass and shown as `[PENDING]` until then.

## Languages and frameworks

All 11 languages plus Solidity ship through the same gate suite. The framework surface is frozen:
adding, removing, or renaming any lane fails the build until the catalogue and the pinned set are
amended together, so the list below and the code that emits it can never disagree.

| Language | Lanes | Framework lanes |
|---|---:|---|
| Python | 11 | Flask, Django, FastAPI, DRF, aiohttp, GraphQL, argparse, Typer, Click, Celery, serverless |
| JavaScript | 5 | Express, Koa, Fastify, GraphQL, serverless |
| TypeScript | 12 | NestJS, Express, Fastify, Hono, Next.js, Angular, React, Vue, Svelte, SvelteKit, GraphQL, serverless |
| Go | 10 | net/http, Gin, Echo, Fiber, Chi, Gorilla, GraphQL, Cobra, serverless, standalone |
| Java | 6 | Spring, Jakarta EE, Quarkus, GraphQL, picocli, serverless |
| Ruby | 3 | Rails, Sinatra, GraphQL |
| PHP | 4 | Laravel, Symfony, Symfony Console, GraphQL |
| Rust | 6 | Actix-web, Axum, Rocket, GraphQL, clap, standalone |
| C | 3 | standalone, host, kernel |
| C++ | 2 | standalone, cpp-httplib |
| Bash | 1 | standalone |
| Solidity | 1 | contract |
| **Total** | **64** | code-language lanes |

The role of a lane is how its handler is shaped: a web framework binds a request, a command-line
lane parses argv, a GraphQL resolver answers a schema field, an event or worker lane drains a queue
or a serverless event, a standalone lane is a plain program or module. **JavaScript and TypeScript
are no longer locked to one framework each.** Earlier releases fixed JavaScript to Koa and
TypeScript to Express; both now draw from the full modern Node surface above.

### Infrastructure substrates (21)

Deploy-time targets an application carries as files in the repository, never as running services:

- **Terraform HCL** (aws, azure, gcp)
- **CloudFormation** (json, yaml)
- **Kubernetes** (manifest, helm, kustomize, ingress)
- **Dockerfile**, **Docker Compose**
- **GitHub Actions**, **GitLab CI**
- **nginx**, **Traefik**
- **In-language IaC** stacks (AWS CDK, CDKTF, Pulumi) for Python and TypeScript

### Pinnable libraries (118)

The corpus renders real third-party libraries rather than toy snippets, so taint flows through the
same APIs a production codebase uses. The pinnable set spans ORMs, database and cache clients,
message-queue clients (Kafka, RabbitMQ, Redis), validators, RPC (gRPC and GraphQL), serialization,
and cloud SDKs, distributed as: Python 18, JavaScript/TypeScript 28, Go 18, Java 20, Ruby 11,
PHP 11, Rust 12.

## The two shapes

### Standalone finding cases

One file per case, single-file taint. Every case models security-relevant behavior using the
applicable components of four axes: where untrusted input enters (**source**), how it travels
(**propagator**), what would neutralize it (**sanitizer or safeguard**), and the dangerous operation
it reaches (**sink**). A vulnerable case omits or defeats the relevant safeguard; its safe twin
applies it correctly. Some cases require companion or shared-runtime files their language or
framework needs; those files are part of their suite's code, not additional cases, so they receive
no separate label.

### Application projects

A new shape: a small, realistic, idiomatic application composed of 2-3 application-tier languages
plus 1-2 cloud or infrastructure targets, varied per app so the shape is not constant for a scanner.
Each project:

- contains a handful of application-tier files with genuine graph structure (nodes, edges, sources,
  sinks, parameters, inter- and intra-procedural flow) for a data-flow engine to traverse;
- carries several planted CWEs, not one, no CWE repeated inside a single application;
- builds under each language's native toolchain as a unit, with real dependency manifests and
  Dockerfiles;
- optionally carries a **compound chain**: the subset of its planted weaknesses that compose into an
  escalation none of the individual findings expresses alone, with a defensive gate on an upstream
  link so the safe variant closes the chain before it reaches the terminal impact.

Combinations are constrained to realistic architectures: no two identical backends stacked, no Rust
on a frontend, no Bash as a backend. A non-idiomatic composition is a build failure rather than a
reviewer's problem.

## How it's built

- **Combinatorial, not hand-written.** The generator combines dozens of components across the four
  axes for each language. Every emitted case is constrained to a valid, analyzable path using real
  language and framework APIs.
- **Synthetic by design.** The corpus intentionally isolates scoring-relevant security properties.
  Individual cases use real APIs but are not intended to represent complete production features.
- **Anti-leakage by construction.** Emitted files carry no comments, no CWE tags, no category names,
  and no label-bearing identifiers. File IDs are shuffled, so filenames do not encode a case's
  category or label. The CSV answer key is the only published source of labels.
- **Seed rotation.** Each release uses a fixed seed. Holding the generator, templates, and toolchain
  constant, the same seed reproduces the corpus byte-for-byte. A new seed emits different
  combinations and identifiers while preserving the benchmark's stated scoring invariants: CWE
  identity, difficulty distribution, 50/50 balance, and language and framework coverage. This limits
  the usefulness of exact-file and filename memorization and is designed to support cross-release
  score comparability.

## What makes it hard

Detecting a bare `eval(input)` is only a baseline. The corpus emphasizes cases intended to exercise
dataflow and safeguard reasoning beyond token or pattern matching:

- **Framework-native APIs.** Real request accessors, DTOs and validation models, ORM and driver
  calls, message-queue clients; the taint flows through idiomatic code, not toy snippets.
- **Broken-safeguard variants.** A safeguard is present but ineffective: a flawed regex,
  wrong-context escaping, or an insufficient length limit. A scanner that trusts the mere presence
  of a safeguard may mislabel the vulnerable case as safe; the corresponding safe case applies an
  effective safeguard for the specified sink.
- **Multi-step taint.** Taint travels from source to sink through propagators such as decoding,
  collection round-trips, and conditional dispatch that a path-insensitive matcher may miss.
- **Cross-boundary taint (application shape).** Untrusted input read in one service reaches a sink in
  another, over HTTP, a message queue, a subprocess, a shared store, or an environment variable, with
  the sink in a different language from the source.

## Scoring

### Standalone scoring

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

Scores are reported in two forms. The **category-averaged** headline score weights each category
equally so large categories cannot dominate; the **flat aggregate** score weights every case equally.
Any tool that emits compatible SARIF 2.1.0 can be scored; the scorer is a single standard-library
Python file with no dependencies.

### Application scoring

A single confusion matrix cannot describe an application, so the result is a triple `(J1, A2, S3)`,
reported side by side and never averaged.

**Layer 1, flow judgment.** The unit is one declared flow. Its truth is `UNSANITIZED`,
`SANITIZED_EFFECTIVE`, or `SANITIZED_BROKEN`. Unsanitized and broken-sanitizer flows expect a finding
(reported = true positive, silent = false negative); an effective sanitizer expects silence
(reported = false positive, silent = true negative). The layer reports sensitivity, specificity, and
Youden's J, plus **broken-sanitizer recall** as a separate sub-metric: the axis that separates a tool
modeling what a sanitizer does from one pattern-matching that a sanitizer was called.

**Layer 2, CWE identification.** The unit is a finding that already matched a truth flow at layer 1,
so a tool cannot farm CWE points by reporting every CWE at every line. Exact CWE scores 1.0, a
correct parent CWE 0.5, wrong 0.

**Layer 3, chain reconstruction.** The unit is the application. To claim the chain, a tool emits a
SARIF `codeFlow` whose `threadFlow` locations, projected to (file, service), cover the true edge
sequence: naming two files in two unrelated findings is not recovery, the ordered pair inside one
path is the evidence that the tool connected them. The layer reports edge recall and, beside it and
never folded into it, CWE recall over every planted weakness (finding 2 of 5 planted CWEs scores 0.4,
regardless of chain outcome). Recovering the entry weakness adds a bonus, so a perfect chain solve
scores above a bare edge match. Reconstructing a graph a tool cannot judge earns nothing: layer 3
counts only for applications whose layer-1 Youden's J clears a floor.

Some applications declare a front-door weakness that is actually controlled. That is a deliberate
contrast case: a tool that reads the working control and correctly stays silent is scored correctly,
not charged a false negative. Applications whose chain genuinely does not complete because an
effective gate blocks it are layer-3 true negatives; a tool claiming a completed chain there is
charged a false positive.

The application shape publishes two answer keys at the suite root. `expectedresults-<version>.csv`
carries one row per flow and one per front door, with eleven columns:

```
key,category,vulnerable,cwe,kind,truth,app_id,archetype,service,file,line
```

`expectedresults-chains-<version>.csv` carries one row per edge of every application, with the entry
and impact facts. `score_apps.py --flows <csv> --chains <csv> --tool-sarif <file>` computes the
triple from those two files alone.

## How the labels are verified

At this scale, "millions of generated files" is a warning sign, not a selling point: auto-generated
code that nothing checked is slop, and a slop benchmark measures nothing. So no file becomes part of
a release until its own toolchain accepts it.

Every emitted file is put through the real, native toolchain for its language before it can ship,
compiled, type-checked, or syntax-checked depending on the language: the Go compiler, `cargo` and
`rustc` for Rust, `javac` and Maven on Java 21, `node` and `tsc` in strict mode for JavaScript and
TypeScript, `php -l`, `ruby -c`, `gcc` and `g++`, and `bash -n`. Not a sample. Every file. On top of
that, a suite of deterministic gates runs with no AI and no LLM-as-judge: each `vulnerable` case must
carry a real source-to-sink taint flow, each `safe` twin must actually neutralize it for that sink,
the recorded sink line must match the scored operation, and dozens of further structural and idiom
checks must hold. The application shape adds a runtime gate: representative projects are built and run
under Docker, and a request to the entry service must produce observable evidence that the terminal
sink executed, before they ship.

That is the bar every case in the release clears. When you cite a score from this corpus you are
trusting its ground truth, and ground truth that never compiled would be worth nothing.

Published bundles contain test code, required support artifacts, CSV answer keys, the scorer,
manifests, checksums, and documentation. Internal per-case proof metadata, the perfect-score oracle
used for self-verification, and the application shape's internal chain ground truth are deliberately
**not** published. The CSVs are the sole published source of labels; test files contain no proof
markers or label metadata from which those labels can be inferred.

## Web-risk category coverage

Standalone coverage against a web-risk taxonomy. Coverage fractions are finalized in the second pass
and shown as `[PENDING]` until then; the scope notes are final.

| Category | Coverage | Scope note |
|---|---|---|
| A01 Broken Access Control | `[PENDING]` | |
| A02 Security Misconfiguration | `[PENDING]` | |
| A03 Software Supply Chain | out of scope | composition analysis, not code-pattern SAST |
| A04 Cryptographic Failures | `[PENDING]` | |
| A05 Injection | `[PENDING]` | |
| A06 Insecure Design | `[PENDING]` | |
| A07 Authentication Failures | `[PENDING]` | |
| A08 Software & Data Integrity | `[PENDING]` | |
| A09 Logging & Alerting Failures | `[PENDING]` | |
| A10 Exceptional Conditions | `[PENDING]` | |

The uncovered items are primarily config-level, supply-chain, or runtime-only concerns outside this
benchmark's current static code-pattern scope.

## Bundles and integrity

Standalone ships as language-size bundles: 11 languages times 3 sizes. Bundles that exceed the
GitHub-release per-file limit are split into parts; the complete part set constitutes the bundle. The
application shape ships as per-suite bundles under `Benchmarks/application/<language>/<framework>/`.
Final bundle counts and byte sizes are shown as `[PENDING]` until the second pass.

Each standalone bundle is self-contained: a `testcode/` directory per framework, the
`expectedresults-<version>.csv` answer key, the bundled `score_sarif.py`, a
`benchproctor-manifest.json` (version, per-framework counts, and SHA-256 checksums), and a README.
Each application bundle carries an `applications/` tree, both published CSV answer keys, and
`score_apps.py`. `SHASUMS256.txt` and per-file checksum sidecars let you verify every download.

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

Corpora are versioned by date (`YYYY.MM.DD`) and released periodically. Each release rotates a fixed
seed: the emitted code changes, while every scoring-relevant invariant (CWE identity, difficulty mix,
50/50 balance, language and framework coverage) stays constant. Last release's score stays
comparable, and a model trained on last release's files learns nothing about this one's. The scorers
use only the Python standard library: clone the repository, point a scorer at a corpus and your
SARIF, and read the resulting metrics.

Per-release facts (case counts, coverage figures, bundle sizes) are recorded per version in
[changelog.md](changelog.md). Shapes and coverage still ahead are tracked in [roadmap.md](roadmap.md).

## License

Apache License 2.0, see [LICENSE](LICENSE). Created and maintained by the author of BenchProctor.
