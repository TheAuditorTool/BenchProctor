# BenchProctor 2026.11.19 -- c (curated tier)

SAST benchmark bundle. Frameworks: standalone.

`<framework>/testcode/` holds labeled vulnerable/safe test cases; each
`<framework>/expectedresults-2026.11.19.csv` is the ground truth (test name, category, vulnerable,
CWE). The bundled `score_sarif.py` (stdlib only, no install) scores a tool's
SARIF output against that CSV.

## Prerequisites

Some cases call a third-party library, because the standard library has no SQL,
HTTP or cryptography API. A tool that compiles the cases, or resolves their
`#include` lines, needs these libraries' development headers:

| Library | Fedora / RHEL | Debian / Ubuntu | Files |
|---|---|---|---|
| OpenSSL | `openssl-devel` | `libssl-dev` | 80 |
| SQLite 3 | `sqlite-devel` | `libsqlite3-dev` | 40 |
| libcurl | `libcurl-devel` | `libcurl4-openssl-dev` | 22 |

    dnf install openssl-devel sqlite-devel libcurl-devel
    apt install libssl-dev libsqlite3-dev libcurl4-openssl-dev

`benchproctor-manifest.json` lists the headers each framework's files include.

## Scan and score

1. Point your SAST tool at a framework's `testcode/` directory and export
   SARIF 2.1.0.
2. Score it against that framework's ground truth:

       python score_sarif.py your_results.sarif standalone/expectedresults-2026.11.19.csv

The scorer prints category-averaged and flat TPR/FPR and a Youden-style score
(TPR - FPR); +100% is perfect, 0% is a coin flip.

## Contents and integrity

- `benchproctor-manifest.json` -- version, per-framework counts, SHA-256 checksums,
  and the libraries each framework's case files include.
- `score_sarif.py` -- the stdlib scorer.
- Every file is listed with its SHA-256 in the `SHASUMS256.txt` at the root of the release
  (`sha256sum -c SHASUMS256.txt` from there).

This bundle contains no answer key beyond the public ground-truth CSV.
