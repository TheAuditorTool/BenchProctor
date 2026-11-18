# BenchProctor 2026.11.16 -- python (curated tier)

Self-contained SAST benchmark bundle. Frameworks: django, fastapi, flask.

`<framework>/testcode/` holds labeled vulnerable/safe test cases; each
`<framework>/expectedresults-2026.11.16.csv` is the ground truth (test name, category, vulnerable,
CWE). The bundled `score_sarif.py` (stdlib only, no install) scores a tool's
SARIF output against that CSV.

## Scan and score

1. Point your SAST tool at a framework's `testcode/` directory and export
   SARIF 2.1.0.
2. Score it against that framework's ground truth:

       python score_sarif.py your_results.sarif django/expectedresults-2026.11.16.csv

The scorer prints category-averaged and flat TPR/FPR and a Youden-style score
(TPR - FPR); +100% is perfect, 0% is a coin flip.

## Contents and integrity

- `benchproctor-manifest.json` -- version, per-framework counts, SHA-256 checksums.
- `score_sarif.py` -- the stdlib scorer.
- Verify this archive itself against the `SHASUMS256.txt` published alongside it.

This bundle contains no answer key beyond the public ground-truth CSV.
