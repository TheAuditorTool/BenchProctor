# Changelog

All notable changes to the BenchProctor published corpus and this repository are recorded here.

Corpora are versioned by release date (`YYYY.MM.DD`). A published release is never silently
replaced: a correction ships as a new release, and a withdrawal is recorded here with its reasons.

Format follows [Keep a Changelog](https://keepachangelog.com/).

## [2026.11.22] - 2026-11-22

A new draw of the whole curated release: every folder under `Benchmarks/` carries this version.
The folders it replaces moved into the archive, which now keeps one zip per release:
2026.11.19's nine languages and applications joined its C and C++ folders in
`archive/2026.11.19.zip`, 2026.11.19.1's C and C++ folders are in `archive/2026.11.19.1.zip`, and
the folder kept for 2026.11.16 became `archive/2026.11.16.zip`. `archive/SHASUMS256.txt` lists the
SHA-256 of every zip.

### Added

- **API generations.** Every framework is drawn in its API generations, each in its own folder
  beside the others: the modern line (`<framework>`), an older line that is still widely deployed
  (`<framework>-legacy`), and the long-term-support line where the project has one
  (`<framework>-lts`). Spring, Jakarta EE, Django and Symfony have all three; the other targets
  have legacy and modern. A class is written in each generation the way that line writes it: its
  framework release, language level and library APIs, including the deprecated APIs an older line
  still uses (`javax.*` on Java 11, `io/ioutil` on a `go 1.20` module, Express 4's `body-parser`,
  pydantic 1 validators, SQLAlchemy 1.4, rand 0.8, bash 3.2 idioms, C99 and C++14). The labels and
  controls are the same in every generation. A target's depth is split across its generations, so
  the release keeps its size: 46 folders over the 21 targets (21 legacy, 4 long-term support, 21
  modern), each with its own answer key, build files and pins. Each application is written in one
  generation of both its services, and each graph's applications are split between legacy and
  modern. The README lists every line.
- **Exact, vetted dependencies.** Every dependency manifest pins exact versions (`package.json`,
  `requirements.txt`, `composer.json`, `Gemfile`, `pom.xml`, `go.mod`, `Cargo.toml`); the
  applications' Node services ship a `package-lock.json` and their Python services a hashed
  `requirements.lock`, and every container image is pinned
  by tag and digest. Versions are the newest stable release of their line published on or before
  2026-10-22, and a later release is taken only where it fixes a published advisory. The legacy
  and long-term-support folders use their own lines' releases, so a dependency scanner reports the
  advisories still open in those lines; they are not part of the ground truth.

### Changed

- **Every weakness class draws from at least three sink forms per side.** In 2026.11.19 most
  classes outside C and C++ rendered a single sink statement per side: every Python SQL injection
  case, for example, called `cursor.execute` on a concatenated string, so a tool that models that
  one call scored the class and a tool that does not scored zero. Each class now ends in at least
  three distinct sink statements per side (a prepared statement built by concatenation and an ORM
  raw query beside the plain query, for SQL injection), and no form is more than 60% of a side.
  The documented exceptions are where a language's own tools offer fewer forms: Bash weak cipher
  (`openssl enc` and `gpg`), Bash XML external entity (`xmllint` and `xsltproc`, and `xmllint`
  alone on the safe side), JavaScript and TypeScript deserialization (`node-serialize` and a YAML
  loader extended with JavaScript types), and PHP deserialization's safe side, where `json_decode`
  can pass 60%. The applications draw the new forms too.
- **Safe server-side request forgery cases rely on a destination allowlist.** Resolving a host,
  checking the address and letting the HTTP client resolve it again is beaten by DNS rebinding,
  so that check no longer counts as a working control in a safe case. The applications'
  unvalidated-URL chain is blocked by an allowlist at its entry service in the same way.
- **The modern generation moves to current releases:** Java 25 with Spring Boot 4.1 and Jakarta EE
  11; Node 24 with Express 5, Koa 3, NestJS 12 and TypeScript 7; Python 3.14 with Django 6.1 and
  FastAPI 0.161; PHP 8.5 with Laravel 13 and Symfony 8.1; Ruby 4.0 with Rails 8.1; Go 1.27; Rust
  edition 2024.
- **The archive keeps one zip per release.** `archive/<version>.zip` holds that release's
  folders and its own `SHASUMS256.txt`, written reproducibly, and `archive/SHASUMS256.txt` lists
  every zip; the latest release stays as plain files under `Benchmarks/`.
- Every language folder carries the `score_sarif.py` with `--categories` and `--skip-categories`,
  and its README and `benchproctor-manifest.json` name the generation and line of every folder.

### Fixed

- **Safe cases a crafted URL could get past.** Some safe open redirect and request forgery cases
  checked the host with a parser that read a URL differently from the browser or the HTTP client
  (a backslash in Python and PHP, userinfo in Bash). Their checks now refuse those URLs.
- **PHP column names on MySQL.** Safe SQL injection cases that quote a column name wrote ANSI
  double quotes by hand. PostgreSQL and SQLite read those as an identifier, but MySQL and MariaDB
  in their default mode read them as a string, where a backslash in the value ends it early; ten
  such cases shipped in 2026.11.19 (Laravel and Symfony). They now quote in the connection's own
  dialect: in Laravel with the driver's quote character, in Symfony with Doctrine's platform
  quoting.
- **Identifiers that named the label.** C and C++ safe cases declared a variable named `safe`, and
  some Java cases used `safeMapper`, `unsafeYamlOpts` and `validatedName`, so a text search could
  sort them. They now use neutral names, and the release build refuses any such identifier.
- **A second weakness in some files**, none of which changed a label: Bash weak cipher passed its
  key on the command line; JavaScript weak cipher used an all-zero key; Bash request forgery cases
  let a URL starting with `-` act as a `curl` option; C and C++ redirect and cookie cases let CR
  and LF split the response; the C and C++ "secure" random tokens were one byte long.
- **Bash integer-overflow safe cases a large value defeated:** with a 19- or 20-digit request, the
  bound check errored out or wrapped to a negative number. The safe sides now bound the length
  first.
- **Application container files that could not build:** the deploy Dockerfiles created their user
  with BusyBox's `adduser -D` on Debian and Ubuntu bases, which have no such option. Each now uses
  the command its base image has.
- **Application services that did not run.** The Jakarta EE services never started: they declared
  no injection manager for Jersey, looked for their resources with a package scan that cannot read
  the packaged service, and declared their resource classes where Jersey could not call them, and a
  resource reading a JSON body had no JSON provider. The Express and NestJS entry services parsed no
  form or multipart body, and NestJS no raw or XML body, so a handler reading one received nothing.
  All of this shipped in 2026.11.19. Before this release, applications of every service graph and
  generation were built, started and sent a request with Docker (see the README's
  [How the labels are verified](README.md#how-the-labels-are-verified)).
- `composer.json` in the PHP folders now lists `phpseclib/phpseclib`, which the weak cipher cases
  use.

Per-language totals:

| Language | Framework targets | Generation folders | Classes per target | Cases |
|---|---|---:|---:|---:|
| Java | Spring, Jakarta EE | 6 | 18 | 1,440 |
| Python | Flask, Django, FastAPI | 7 | 18 | 2,160 |
| Go | Gin, net/http | 4 | 15 | 1,200 |
| Rust | Actix-web, Axum | 4 | 15 | 1,200 |
| TypeScript | NestJS, Express | 4 | 18 | 1,440 |
| JavaScript | Express, Koa | 4 | 18 | 1,440 |
| PHP | Laravel, Symfony | 5 | 18 | 1,440 |
| Ruby | Rails, Sinatra | 4 | 17 | 1,360 |
| C++ | cpp-httplib, standalone | 4 | 22 | 2,112 |
| C | standalone | 2 | 19 | 1,140 |
| Bash | standalone | 2 | 11 | 440 |
| **All 11 languages** | **21** | **46** | **25 in union** | **15,372** |

Applications: 368 over six graphs, 5,284 labeled flows (1,460 vulnerable, 3,824 safe).

## [2026.11.19.1] - 2026-11-19 (C and C++)

A deeper C and C++ draw, published the same day as 2026.11.19. Only `Benchmarks/standalone/c` and
`Benchmarks/standalone/cpp` change; the other nine languages and the applications stay at
2026.11.19. The 2026.11.19 C and C++ folders moved to
[`archive/2026.11.19/`](archive/2026.11.19/) with their own `SHASUMS256.txt`.

### Changed

- **Each C and C++ memory-safety and integer-overflow class draws from three sink forms.** In
  2026.11.19 every case of a class used one sink statement. In `use_after_free`, for example,
  every vulnerable case printed the freed pointer with `printf`, so a tool that does not model
  `printf` scored zero on the whole class. The labels were right; the class tested one shape. Now:
  - stack and heap buffer overflow: `strcpy`, `memcpy` of the input's length and terminator,
    `sprintf` into a fixed buffer;
  - buffer over-read: a read loop, `memcpy` out of the buffer, `fwrite` (C) or `cout.write` (C++)
    of an input-sized span;
  - use after free: the freed pointer printed, dereferenced, or wiped with `memset`;
  - integer overflow: `atoi(x) + 1` into an allocation, a count times a record size into an
    allocation, a quantity times a unit price.
- **Deeper sampling:** 30 vulnerable + 30 safe cases per class in C (1,140 cases, up from 640)
  and 24 + 24 per class and framework in C++ (2,112, up from 1,520).
- The bundled `score_sarif.py` in the C and C++ folders takes `--categories` and
  `--skip-categories` (see the scorer update below).

### Added

- **Three C and C++ classes:** double free (CWE-415), memory leak (CWE-401) and use of an
  uninitialized variable (CWE-457), each with three sink forms: a pointer freed through an alias,
  on an error branch and again on the normal path, or twice by a cleanup loop; a block never
  freed, skipped by an early return, or lost when its only pointer is overwritten; an array slot
  or branch-only scalar, a struct field never set, or a branch chain without a final `else`.

Per-language totals (only C and C++ changed):

| Language | Framework targets | Classes per target | Cases |
|---|---|---:|---:|
| C++ | cpp-httplib, standalone | 22 | 2,112 |
| C | standalone | 19 | 1,140 |
| **All 11 languages** | **21** | **25 in union** | **15,372** |

## [Scorer update] - 2026-11-19

### Changed

- **`scripts/score_sarif.py` scores a declared scope.** `--categories` scores only the listed
  classes and `--skip-categories` leaves the listed ones out, so a tool that does not attempt a
  class (an analyzer that does no LDAP checking, say) is not averaged over it. The summary names
  the classes left out. A class name not in the answer key, or an unknown option, is now refused
  instead of silently ignored.
- The summary described a 0% score as "random guessing (no better than a coin flip)". It now
  reads "no measured discrimination", as this README always has: flagging every case and
  flagging none both score 0%, and so does a class a tool does not attempt.
- The copies bundled in release 2026.11.19's language folders are part of that release and are
  unchanged; the C and C++ folders of 2026.11.19.1 carry the new scorer, and the other language
  folders pick it up in their next release.

## [2026.11.19] - 2026-11-19

A rotation of the curated release with deeper sampling and two more application graphs, published
as plain files instead of zips. Every folder under `Benchmarks/` carries this version.

### Changed

- **Published as plain files.** The cases and answer keys are regular files under `Benchmarks/`,
  readable here without downloading or unpacking anything, with one `SHASUMS256.txt` over every
  file. Release 2026.11.16 moved to [`archive/2026.11.16/`](archive/2026.11.16/), unpacked, with
  its own `SHASUMS256.txt`; its original zips remain in this repository's history.
- **20 vulnerable + 20 safe cases per framework and class pair**, up from 3: 14,280 standalone
  cases over the same 357 pairs (11 languages, 21 framework targets, 22 weakness classes). One case
  now moves a framework's headline score by well under one point.
- **368 applications over 6 service graphs**, up from 60 over 4, at 4 applications per class and
  side on each graph: 5,299 labeled flows, 1,473 vulnerable and 3,826 safe. Two graphs are new, and
  they are the first that do not start in JavaScript or TypeScript: FastAPI to Spring (Python to
  Java) and Jakarta EE to NestJS (Java to TypeScript).

### Added

- **Dependency manifests for every standalone framework.** Each Python, JavaScript, TypeScript, PHP
  and Ruby framework folder carries `requirements.txt`, `package.json`, `composer.json` or a
  `Gemfile`, derived from what its cases import, as Java, Go and Rust already did with `pom.xml`,
  `go.mod` and `Cargo.toml`. A tool that resolves types can install exactly what the cases use.
- Each standalone folder's README and `benchproctor-manifest.json` list the third-party libraries
  its C and C++ cases include, with their Fedora and Debian packages.

### Fixed

- The C cases' build prerequisites are documented (issue #1). In 2026.11.16, 22 of the 96 C cases
  called SQLite, libcurl or OpenSSL and nothing said so; the README's
  [C and C++ prerequisites](README.md#c-and-c-prerequisites) section gives the packages. In
  2026.11.19, 142 of the 640 C cases and 17 of the 1,520 C++ cases need a library.

Per-language totals:

| Language | Framework targets | Cases |
|---|---|---:|
| Java | 2 | 1,440 |
| Python | 3 | 2,160 |
| Go | 2 | 1,200 |
| Rust | 2 | 1,200 |
| TypeScript | 2 | 1,440 |
| JavaScript | 2 | 1,440 |
| PHP | 2 | 1,440 |
| Ruby | 2 | 1,360 |
| C++ | 2 | 1,520 |
| C | 1 | 640 |
| Bash | 1 | 440 |
| **Total** | **21** | **14,280** |

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
