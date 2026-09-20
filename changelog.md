# Changelog

All notable changes to the BenchProctor published corpus and this repository are recorded here.

Corpora are versioned by release date (`YYYY.MM.DD`) and are immutable once published: corrections
ship as a new dated release, never as a silent replacement. This file, not the README, is the home
for per-release facts such as case counts, language coverage, and bundle sizes. The README describes
the project in general terms; the numbers that change every release live here.

Format follows [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased] (documented as v2.0)

The largest change since the first corpus. The next release ships two shapes together, standalone
and application, on a far larger and fully unlocked framework surface. It stays date-versioned
(`YYYY.MM.DD`); the README frames it as v2.0 to signal the scale of the change. Corpus counts below
are `[PENDING]` until the release clears its acceptance gates.

### Added

- **Application shape.** Small, buildable polyglot projects composed of 2-3 application-tier
  languages plus 1-2 cloud or infrastructure targets, each carrying several planted CWEs and, where
  the archetype allows, a compound chain that escalates across services. Every project builds under
  its native toolchains as a unit and passes a Docker runtime gate before release.
- **Three-layer application scoring.** The application shape is scored as a triple `(J1, A2, S3)`:
  flow judgment, CWE identification, and chain reconstruction, reported side by side and never
  averaged into one number. It publishes two answer keys at the suite root
  (`expectedresults-<version>.csv` and `expectedresults-chains-<version>.csv`) and a `score_apps.py`
  that computes the triple from those two files alone.
- **Solidity contract emitter**, taking the corpus to 11 general-purpose languages plus Solidity.
- **Full frozen framework surface.** 85 requestable lanes (64 code-language lanes plus 21
  infrastructure substrates), drawing on 118 pinnable third-party libraries. Every web language gains
  a GraphQL resolver lane, and most gain command-line and serverless or worker lanes. Infrastructure
  substrates cover Terraform HCL, CloudFormation, Kubernetes, Dockerfile, Docker Compose, GitHub
  Actions, GitLab CI, nginx, Traefik, and the in-language AWS CDK, CDKTF, and Pulumi stacks.
- **JavaScript and TypeScript unlocked.** Earlier releases fixed JavaScript to Koa and TypeScript to
  Express. JavaScript now draws from Express, Koa, Fastify, GraphQL, and serverless; TypeScript from
  NestJS, Express, Fastify, Hono, Next.js, Angular, React, Vue, Svelte, SvelteKit, GraphQL, and
  serverless.

### Changed

- **README rewritten** to document both shapes and the full framework surface, framed as v2.0. The
  standalone scoring model (Youden's J) is unchanged.
- **Per-release statistics moved out of the README.** Case totals, coverage figures, bundle sizes,
  and per-language counts no longer live in `README.md`; they are recorded here per release instead.
  These were release-specific facts that a general project README should not have carried in the
  first place. This entry records that relocation retroactively; the figures themselves are preserved
  in the release entries below.

### Pending

- All v2.0 corpus counts: total labeled cases, per-size and per-language totals, category and CWE
  counts, web-risk coverage fractions, application archetype count, and final bundle counts and
  sizes. Filled in once the release completes its gate suite.

## [2026.07.22] - 2026-07-23

Full standalone corpus: all 11 languages as single-file finding cases. This is the currently shipped
release; every bundle under `Benchmarks/` carries this version.

### Added

- All 11 languages (Java, Python, Go, Rust, TypeScript, JavaScript, PHP, Ruby, Bash, C, C++) across
  21 framework targets, in three sizes (`quicktest`, `normal`, `enterprise`).
- **2,938,418 labeled cases**, split exactly 50 / 50: 1,469,209 vulnerable and 1,469,209 safe.
- 242 emitted categories mapped to 231 distinct CWE IDs.
- 2,172 companion and shared-runtime files required by some cases; part of their suite's code, not
  scored separately.

Per-size totals:

| Size | Vulnerable | Safe | Total |
|---|---:|---:|---:|
| `quicktest` | 59,100 | 59,100 | 118,200 |
| `normal` | 420,333 | 420,333 | 840,666 |
| `enterprise` | 989,776 | 989,776 | 1,979,552 |
| **Total** | **1,469,209** | **1,469,209** | **2,938,418** |

Per-language totals:

| Language | Framework targets | Labeled cases |
|---|---|---:|
| Java | Spring, Jakarta EE | 307,556 |
| Python | Flask, Django, FastAPI | 447,132 |
| Go | Gin, net/http | 284,096 |
| Rust | Actix-web, Axum | 282,448 |
| TypeScript | NestJS, Express | 304,696 |
| JavaScript | Express, Koa | 304,696 |
| PHP | Laravel, Symfony | 299,156 |
| Ruby | Rails, Sinatra | 295,016 |
| C++ | cpp-httplib, standalone | 247,512 |
| C | standalone | 49,520 |
| Bash | standalone | 116,590 |

### Bundles

- 33 logical language-size bundles (11 languages times 3 sizes). Six enterprise bundles exceeded the
  per-file limit and were split into two parts, producing 39 final ZIP files.
- The final ZIP set occupies 1,587,819,973 bytes (1,514.3 MiB), verified by `SHASUMS256.txt` and
  per-file checksum sidecars.

### Docs

- Corrected the shipped web-risk coverage figures: 205 of 249 mapped CWEs covered (82.3%).
- Added the toolchain-verified, no-slop due-diligence description of how labels are verified.

## [2026.2] - 2026-06-22

First published corpus: Java and Python standalone finding cases only, as the start of a phased
language rollout. Superseded by `2026.07.22`, which added the remaining nine languages.

## [Initial] - 2026-05-30

First public repository: the standard-library SARIF scorer, the Apache-2.0 license, and the
BenchProctor scope and positioning. Tooling and documentation only, no corpus bundles yet.
