# BenchProctor 2026.11.22 -- cpp (curated tier)

SAST benchmark bundle. Frameworks: httplib, httplib-legacy, standalone, standalone-legacy.

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
| `httplib` | modern | C++20 on cpp-httplib |
| `httplib-legacy` | legacy | C++14 on cpp-httplib, POSIX file calls in place of std::filesystem |
| `standalone` | modern | C++20 with std::filesystem |
| `standalone-legacy` | legacy | C++14: POSIX directory and file calls where C++17 has std::filesystem |

## Prerequisites

Some cases call a third-party library, because the standard library has no SQL,
HTTP or cryptography API. A tool that compiles the cases, or resolves their
`#include` lines, needs these libraries' development headers:

| Library | Fedora / RHEL | Debian / Ubuntu | Files |
|---|---|---|---|
| RabbitMQ C client | `librabbitmq-devel` | `librabbitmq-dev` | 11 |
| hiredis | `hiredis-devel` | `libhiredis-dev` | 7 |

    dnf install librabbitmq-devel hiredis-devel
    apt install librabbitmq-dev libhiredis-dev

`benchproctor-manifest.json` lists the headers each framework's files include.

## Scan and score

1. Point your SAST tool at a framework's `testcode/` directory and export
   SARIF 2.1.0.
2. Score it against that framework's ground truth:

       python score_sarif.py your_results.sarif httplib/expectedresults-2026.11.22.csv

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
