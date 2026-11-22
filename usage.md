# Using BenchProctor

The operational guide: how to pick the cases you want, run a scanner against them, and read the
score. For what the release is and why it is built the way it is, see [README.md](README.md); for
the release history, see [changelog.md](changelog.md).

The current release is `2026.11.22`: 15,372 standalone cases, one file per case, in all 11
languages, and 368 multi-service applications. It is published as plain files in `Benchmarks/`;
nothing needs unpacking. Earlier releases are under [`archive/`](archive/), one zip per release.

## 1. Pick your cases

A standalone language folder holds every framework for that language, one folder per framework
and API generation, so you choose the framework and the generation inside it.

```
Benchmarks/standalone/<language>/
Benchmarks/applications/
```

- "I want Java" -> `Benchmarks/standalone/java/`, then `spring/` (Spring Boot 4.1 on Java 25),
  `spring-lts/` (Boot 3.5 on Java 21) or `spring-legacy/` (Boot 2.7 on Java 11), or the same three
  for `jakarta`.
- "I want Python, FastAPI" -> `Benchmarks/standalone/python/fastapi/` (FastAPI 0.161 with
  pydantic 2) or `fastapi-legacy/` (FastAPI 0.99 with pydantic 1).
- "I want the multi-service applications" -> `Benchmarks/applications/`, then one service-graph
  folder in it.

`<framework>` is always the modern generation, `<framework>-lts` the long-term-support line where
the project has one, and `<framework>-legacy` an older line that is still widely deployed. The
README's [Generations](README.md#generations) table lists every line, and each language folder's
README lists the folders it holds.

## 2. What is inside a standalone language folder

Labels live only in the CSV answer keys. The test files themselves carry no comments, CWE tags, or
label-bearing names, so you cannot infer a label from a file.

```
Benchmarks/standalone/<language>/
  score_sarif.py                     the scorer (standard-library Python, no dependencies)
  benchproctor-manifest.json         version, per-folder counts, generation and line, checksums, C/C++ libraries
  README.md                          folder-local notes, including what each generation folder targets
  <framework>[-legacy|-lts]/
    testcode/                        the cases you scan
    expectedresults-2026.11.22.csv   the answer key for this folder
```

Every framework folder except C, C++ and Bash also carries its language's dependency manifest next
to `testcode/`, listing the packages its cases import at exact versions of that generation's line:
`pom.xml`, `go.mod` and `go.sum`, `Cargo.toml`, `requirements.txt`,
`package.json`, `composer.json` or `Gemfile`. Install from it when your tool resolves types or you
want to run a case. Some frameworks carry other build files their toolchain needs, such as
`tsconfig.json`. None of them hold labels.

Compiling some C and C++ cases needs a library's development headers (SQLite, libcurl and OpenSSL
for C; hiredis and the RabbitMQ C client for C++), because neither standard library has an SQL,
HTTP, cryptography or message-queue API. See
[C and C++ prerequisites](README.md#c-and-c-prerequisites) for the install commands.

## 3. Run and score a standalone folder

```bash
# scan one folder's testcode and export SARIF 2.1.0
your-tool scan Benchmarks/standalone/java/spring/testcode --format sarif -o results.sarif

# score against that folder's answer key
python Benchmarks/standalone/java/score_sarif.py results.sarif \
  Benchmarks/standalone/java/spring/expectedresults-2026.11.22.csv
```

Score each generation folder against its own answer key: test names restart in every folder, so
one SARIF file per folder keeps the matching unambiguous.

The scorer matches a finding to a case by file and recovers the finding's CWE from the SARIF
`ruleId`, the result or rule `properties` or `tags` (for example `external/cwe/cwe-089`), or CWE
`taxa`. If your tool emits no CWE at all, add `--match-mode filename`: any finding on a vulnerable
file then counts. That mode rewards over-flagging, so prefer the default when your tool emits CWEs.

If your tool does not attempt some classes, declare its scope: `--skip-categories ldapi,sqli`
leaves those classes out, and `--categories null_deref,use_after_free` scores only those. The
summary names every class left out. The scorer in `scripts/` and the copy in every language
folder have these options.

### Reading the output

The scorer prints a confusion matrix and, from it, three numbers:

- `TPR` (true-positive rate): the share of vulnerable cases your tool flagged.
- `FPR` (false-positive rate): the share of safe cases your tool flagged.
- `J` (Youden's J = TPR - FPR): the headline score.

`J` is reported two ways. **Category-averaged** weights each class equally, so a few large classes
cannot dominate; **flat aggregate** weights every case equally. A perfect tool scores `J = +100%`.
A flag-everything or flag-nothing tool scores `0%`, because its TPR and FPR are equal. A tool that
flags safe code and misses real bugs scores below zero.

A framework's 20 vulnerable and 20 safe cases per class are split across its generations: 10 and
10 per folder over two generations, 7, 7 and 6 over three (15 in C, 12 in C++). One case moves one
class in one folder by ten points (about fifteen with seven per side), and the folder's headline
score by under one point.

## 4. The applications

```
Benchmarks/applications/
  score_apps.py                             the scorer (standard-library Python, no dependencies)
  benchproctor-manifest.json                version, counts, SHA-256 checksums
  README.md                                 folder-local notes
  <service-graph>/
    applications/<application>/             one project: docker-compose.yml and services/<service>/
    expectedresults-2026.11.22.csv          one row per labeled flow, with its file and line
    expectedresults-chains-2026.11.22.csv   the service graph and whether the chain completes
```

Each application is written in one generation of both its services, legacy or modern, and each
graph holds both; a service's dependency manifest, lockfile and Dockerfile name the releases it
targets. Scan a service graph's `applications/` directory as one tree, then score it:

```bash
your-tool scan Benchmarks/applications/nestjs-spring/applications --format sarif -o results.sarif
python Benchmarks/applications/score_apps.py \
  --flows  Benchmarks/applications/nestjs-spring/expectedresults-2026.11.22.csv \
  --chains Benchmarks/applications/nestjs-spring/expectedresults-chains-2026.11.22.csv \
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

## 5. Verify the files

Every published file is listed with its SHA-256. From the `Benchmarks/` directory:

```bash
sha256sum -c SHASUMS256.txt
```

For an archived release, check the zip against `archive/SHASUMS256.txt`, unzip it, and run the
same check inside the release folder it holds:

```bash
cd archive && sha256sum -c SHASUMS256.txt --ignore-missing
unzip 2026.11.19.zip -d /some/where && cd /some/where/2026.11.19 && sha256sum -c SHASUMS256.txt
```

## FAQ

**Why is the split exactly 50 / 50 vulnerable and safe?**
So a tool cannot game the score by flagging everything. Under Youden's J, a flag-everything tool has
a 100% true-positive rate and a 100% false-positive rate, which nets to zero. The applications are
not 50 / 50: most of the code in a real project is safe, and so it is there.

**Which generation should I score?**
All of them, each on its own. The modern folder shows how a tool handles current releases; the
legacy and long-term-support folders show whether it still recognizes the same weaknesses written
against the older APIs that much deployed code uses. Report the folders side by side rather than
pooled.

**My dependency scanner reports vulnerable packages in the legacy folders. Is that a defect?**
No. The legacy and long-term-support folders use the releases of their own lines, and some of those
lines carry published advisories, as such code does in the field. The answer keys label the code's
weaknesses only; dependency advisories are not part of the ground truth.

**Why is the release curated rather than the whole corpus?**
Twenty cases per side for each framework and class is enough to score a language or a class
closely, and each release is a fresh draw, so a tool cannot be tuned to the files.

**Where are the earlier releases?**
Under [`archive/`](archive/), one zip per release (`archive/<version>.zip`), kept unchanged and
listed with its SHA-256 in `archive/SHASUMS256.txt`. Each zip holds that release's folders and its
own `SHASUMS256.txt`.

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
