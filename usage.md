# Using BenchProctor

The operational guide: how to pick the exact corpus you want, run a scanner against it, and read the
score. For what the corpus is and why it is built the way it is, see [README.md](README.md); for
per-release numbers, see [changelog.md](changelog.md).

There are two shapes. Standalone is single-file finding cases. Application is deployable polyglot
projects whose taint crosses files, languages, and processes. You pick one shape, then narrow to the
exact bundle.

## 1. Pick your corpus

### Standalone: size, then language, then framework

A standalone bundle is one `(language, size)` pair. Sizes are `quicktest` (fastest, most prevalent
classes), `normal` (the headline scoreable corpus), and `enterprise` (deepest sampling). Each bundle
holds every framework for that language, so you choose the framework inside the bundle.

```
Benchmarks/<size>/<language>/benchproctor-<language>-<size>-<version>.zip
```

Large enterprise bundles are split into `part1of2` and `part2of2`; download both, they extract into
one tree.

- "I want standalone Java, quicktest" ->
  `Benchmarks/quicktest/java/benchproctor-java-quicktest-<version>.zip`, then the `spring/` or
  `jakarta/` framework subtree inside it.
- "I want standalone Python, normal, FastAPI" ->
  `Benchmarks/normal/python/benchproctor-python-normal-<version>.zip`, then the `fastapi/` subtree.

The framework names for each language are listed in the README's
[Languages and frameworks](README.md#languages-and-frameworks) catalogue.

### Application: the (language, framework) suite

An application bundle is one code `(language, framework)` suite. The applications inside it are
whole projects that also carry their declared cloud or infrastructure targets as files.

```
Benchmarks/application/<language>/<framework>/benchproctor-apps-<language>-<framework>-<version>.zip
```

- "I want apps Django" ->
  `Benchmarks/application/python/django/benchproctor-apps-python-django-<version>.zip`.

## 2. What is inside a bundle

Labels live only in the CSV answer keys. The test files themselves carry no comments, CWE tags, or
label-bearing names, so you cannot infer a label from a file.

### Standalone bundle

```
benchproctor-<language>-<size>/
  score_sarif.py                     the scorer (standard-library Python, no dependencies)
  benchproctor-manifest.json         version, per-framework counts, SHA-256 checksums
  README                             bundle-local notes
  <framework>/
    testcode/                        the cases you scan
    expectedresults-<version>.csv    the answer key for this framework
```

### Application bundle

```
benchproctor-apps-<language>-<framework>/
  score_apps.py                          the application scorer
  applications/                          the project trees you scan
  expectedresults-<version>.csv          one row per flow and per front door
  expectedresults-chains-<version>.csv   one row per edge of every application
  README                                 bundle-local notes
```

## 3. Run and score: standalone

```bash
# extract
unzip Benchmarks/normal/java/benchproctor-java-normal-<version>.zip -d benchproctor-java-normal

# scan one framework's testcode and export SARIF 2.1.0
your-tool scan ./benchproctor-java-normal/spring/testcode --format sarif -o results.sarif

# score against that framework's answer key
python ./benchproctor-java-normal/score_sarif.py results.sarif \
  ./benchproctor-java-normal/spring/expectedresults-<version>.csv
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

`J` is reported two ways. **Category-averaged** weights each category equally, so a few large
categories cannot dominate; **flat aggregate** weights every case equally. A perfect tool scores
`J = +100%`. A flag-everything or flag-nothing tool scores `0%`, because its TPR and FPR are equal.
A tool that flags safe code and misses real bugs scores below zero.

## 4. Run and score: application

```bash
# extract
unzip Benchmarks/application/python/django/benchproctor-apps-python-django-<version>.zip -d apps

# scan the whole application tree. Emit SARIF codeFlow so the scorer can credit chain recovery.
your-tool scan ./apps/applications --format sarif -o results.sarif

# score against the two published answer keys
python ./apps/score_apps.py \
  --flows  ./apps/expectedresults-<version>.csv \
  --chains ./apps/expectedresults-chains-<version>.csv \
  --tool-sarif results.sarif
```

### Reading the output

The application scorer reports a triple, `(J1, A2, S3)`, side by side. It never averages them,
because one number would hide which of the three a tool is weak at.

- `J1`, flow judgment: sensitivity, specificity, and Youden's J over the declared flows, plus a
  separate **broken-sanitizer recall** figure. Broken-sanitizer recall is the axis that separates a
  tool that models what a sanitizer does from one that pattern-matches that a sanitizer was called.
- `A2`, CWE identification: how well findings that already matched a real flow name the right CWE.
  An exact CWE scores full credit, a correct parent CWE half.
- `S3`, chain reconstruction: whether the tool reconnected the planted escalation across services,
  reported beside a CWE-recall figure over every planted weakness.

To earn `S3` credit your SARIF must include a `codeFlow` whose ordered `threadFlow` locations cover
the true edge sequence. Naming two files in two unrelated findings is not chain recovery; the ordered
path inside one finding is the evidence that your tool connected them. The full definition of each
layer is in the README's [Application scoring](README.md#application-scoring) section.

## 5. Verify your download

Every published file is checksummed. From the `Benchmarks/` directory:

```bash
sha256sum -c SHASUMS256.txt
```

Per-file checksum sidecars accompany the bundles for spot verification.

## FAQ

**Why is the split exactly 50 / 50 vulnerable and safe?**
So a tool cannot game the score by flagging everything. Under Youden's J, a flag-everything tool has
a 100% true-positive rate and a 100% false-positive rate, which nets to zero.

**Can I train a model on the corpus?**
Each release rotates a fixed seed, so the emitted code changes every release while the scoring
invariants stay constant. A model trained on one release learns little about the next. As with any
benchmark, do not train on the exact corpus you then report a score against.

**My tool does not emit CWE identifiers. Can I still score?**
For standalone, yes: `--match-mode filename` counts any finding on a vulnerable file. It rewards
over-flagging, so treat those numbers as a floor, not a like-for-like comparison with CWE-aware runs.

**Which SARIF fields does the scorer read for the CWE?**
`ruleId`, the result or rule `properties` and `tags` (for example `external/cwe/cwe-089`), and CWE
`taxa`. This covers the common SARIF 2.1.0 encodings without configuration.

**Are labels hidden in the filenames?**
No. File IDs are shuffled and carry no category or label information. The CSV answer keys are the only
source of labels.

**I think a label is wrong. How do I report it?**
Open a ground-truth challenge that names the affected case, its published label, and the semantic
basis for disputing it. Confirmed defects are corrected in a new dated release; published answer keys
are never silently replaced. See the README's
[Corrections and ground-truth disputes](README.md#corrections-and-ground-truth-disputes) section.

**Which Python do I need for the scorers?**
Any Python 3. Both `score_sarif.py` and `score_apps.py` use only the standard library and have no
dependencies.

**How do scores compare across releases?**
Releases are date-versioned and immutable. Seed rotation keeps CWE identity, difficulty mix, the
50 / 50 balance, and language and framework coverage constant, so a score from one release stays
comparable to the next.
