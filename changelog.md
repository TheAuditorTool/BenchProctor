# Changelog

All notable changes to the BenchProctor published corpus and this repository are recorded here.

Corpora are versioned by release date (`YYYY.MM.DD`). A published release is never silently
replaced: a correction ships as a new release, and a withdrawal is recorded here with its reasons.

Format follows [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

### Fixed

- The C cases' build prerequisites are now documented (issue #1). 22 of the 96 C cases in
  2026.11.16 call SQLite, libcurl or OpenSSL, and nothing said so; the README's new
  [C prerequisites](README.md#c-prerequisites) section gives the packages. The bundles are
  unchanged. From the next release, each bundle's README and manifest list the libraries its
  files include.

## [2026.11.16] - 2026-11-16

Releases resume as a curated release: a small, fresh draw, easy and medium difficulty only, on a
fixed list of frameworks and weakness classes. Every bundle under `Benchmarks/` carries this
version.

### Added

- **2,142 standalone cases**, split exactly 50 / 50: 1,071 vulnerable and 1,071 safe. All 11
  languages across the same 21 framework targets as before, 22 weakness classes mapped to 22
  distinct CWE IDs, and 3 vulnerable + 3 safe cases for each of the 357 framework and class pairs.
- **60 multi-service applications**, new in this release: two services that call each other over
  HTTP, each with its own container file, in TypeScript, JavaScript, Python, Java and C++. They
  hold 860 labeled flows (234 vulnerable, 626 safe) over 4 service graphs.
- `scripts/score_apps.py`, the standard-library scorer for the applications. It reports flow
  judgment, CWE identification and chain reconstruction side by side.

Per-language totals:

| Language | Framework targets | Cases |
|---|---|---:|
| Java | Spring, Jakarta EE | 216 |
| Python | Flask, Django, FastAPI | 324 |
| Go | Gin, net/http | 180 |
| Rust | Actix-web, Axum | 180 |
| TypeScript | NestJS, Express | 216 |
| JavaScript | Express, Koa | 216 |
| PHP | Laravel, Symfony | 216 |
| Ruby | Rails, Sinatra | 204 |
| C++ | cpp-httplib, standalone | 228 |
| C | standalone | 96 |
| Bash | standalone | 66 |

### Changed

- **Scope.** This release contains no case built around an ineffective safeguard and none of the
  deepest propagation patterns. A vulnerable case has no safeguard; a safe case has one that works.
- **Sizes.** There is one size. The `quicktest`, `normal` and `enterprise` sizes are gone.
- **Archives.** One ZIP per language and one for the applications, with forward-slash paths. They
  extract with any standard tool.
- **`score_sarif.py`.** The score legend printed doubled percent signs (`+100%%`); it now prints
  `+100%`. Scoring is unchanged.

### Removed

- **Release 2026.07.22 is withdrawn**, and its bundles are removed from this repository together with
  its history. An audit before this release found, in families that release was built from:
  - a wrong `safe` label on 314 cases: some safe SQL injection cases guarded the value with a
    character allowlist and then placed it unquoted in the statement, which left them exploitable
    (the input `id` turns `WHERE id = id` into a condition that matches every row). A scan of
    every file in the withdrawn bundles found 116 in Java and 198 in Python, and none in the other
    nine languages. By size: `quicktest` 58, `normal` 87, `enterprise` 169. Direction of the
    change: `safe` cases that should have been `vulnerable`;
  - safe cases whose dangerous line could never run, because the value was wrapped in fixed text
    and then checked as a whole. The label was right; the case tested nothing;
  - request handlers in Java, Rust and Ruby that read command-line input, an entry point that
    cannot occur in a deployed service. No label was wrong;
  - unidiomatic Java: unused imports, a persistence factory built on every request, and repository
    types declared inside a handler. No label was affected.

  Only the first item changed a label. Scores reported against 2026.07.22 should not be compared
  with scores on any later release.

## [Releases halted] - 2026-10-09

Further releases are halted indefinitely, until we choose otherwise, due to the nature of
competition and the AI industry converging towards SAST-based solutions. Release `2026.07.22`
remains the latest published corpus, and every bundle under `Benchmarks/` still carries that version.
The halt ended on 2026-11-16 with release `2026.11.16`, in curated form.

### Removed

- The documentation for a planned next release. It described an application shape, a wider
  framework surface, and a Solidity emitter; that release will not ship, so the README, usage guide,
  and roadmap now describe the published `2026.07.22` corpus only.

### Changed

- **How the labels are verified, corrected.** Before release, one case for every sink and sanitizer
  combination, in every language and framework, was compiled or syntax-checked by its native
  toolchain. The published sizes add source and propagator variants around those combinations that
  were not each compiled individually. The earlier "every file" wording overstated this.
- **Extracting on Linux and macOS, documented.** The `2026.07.22` archives store paths with Windows
  `\` separators. `unzip` prints a warning and converts them to folders; some other extractors, such
  as Python's `zipfile` module, keep the `\` in the file names.

## [2026.07.22] - 2026-07-23 (withdrawn 2026-11-16)

Full standalone corpus: all 11 languages as single-file finding cases. Withdrawn on 2026-11-16;
see `2026.11.16` above for the reasons. Its bundles are no longer distributed.

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
