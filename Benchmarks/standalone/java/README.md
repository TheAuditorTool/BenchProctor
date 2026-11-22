# BenchProctor 2026.11.22 -- java (curated tier)

SAST benchmark bundle. Frameworks: jakarta, jakarta-legacy, jakarta-lts, spring, spring-legacy, spring-lts.

`<framework>/testcode/` holds labeled vulnerable/safe test cases; each
`<framework>/expectedresults-2026.11.22.csv` is the ground truth (test name, category, vulnerable,
CWE). The bundled `score_sarif.py` (stdlib only, no install) scores a tool's
SARIF output against that CSV.

## Generations

Each framework is drawn in each of its API generations, one folder per generation:
`<framework>` is the modern line, `<framework>-lts` the long-term-support line where the
project has one, and `<framework>-legacy` an older line still widely deployed. The classes,
labels and controls are the same in every generation; what differs is how the code is
written: the framework release, the language level and the library APIs. Each folder has its
own ground truth, build files and dependency pins, and is drawn separately, so the folders
hold different cases.

| Folder | Generation | Line |
|---|---|---|
| `jakarta` | modern | Jakarta EE 11 (Servlet 6.1, Jersey 4), Java 25 |
| `jakarta-lts` | LTS | Jakarta EE 10 (Servlet 6.0, Jersey 3.1), Java 21 |
| `jakarta-legacy` | legacy | Java EE 8 (javax.ws.rs 2.1, Servlet 4, Jersey 2), Java 11 |
| `spring` | modern | Spring Boot 4.1, Java 25, Jakarta EE 11 |
| `spring-lts` | LTS | Spring Boot 3.5, Java 21, jakarta.\* |
| `spring-legacy` | legacy | Spring Boot 2.7, Java 11, javax.\* |

## Scan and score

1. Point your SAST tool at a framework's `testcode/` directory and export
   SARIF 2.1.0.
2. Score it against that framework's ground truth:

       python score_sarif.py your_results.sarif jakarta/expectedresults-2026.11.22.csv

The scorer prints category-averaged and flat TPR/FPR and a Youden-style score
(TPR - FPR); +100% is perfect, and 0% means no measured discrimination (flagging
every case and flagging none both score 0%). `--categories` or `--skip-categories`
scores only the categories a tool declares in scope.

## Contents and integrity

- `benchproctor-manifest.json` -- version, per-framework counts, SHA-256 checksums,
  and the libraries each framework's case files include.
- `score_sarif.py` -- the stdlib scorer.
- Every file is listed with its SHA-256 in the `SHASUMS256.txt` at the root of the release
  (`sha256sum -c SHASUMS256.txt` from there).

This bundle contains no answer key beyond the public ground-truth CSV.
