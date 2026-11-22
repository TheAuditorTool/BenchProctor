# BenchProctor Apps 2026.11.22 -- applications (curated tier)

Self-contained SAST benchmark bundle of multi-service APPLICATIONS.
Frameworks: express-django, express_ts-flask, express_ts-httplib, fastapi-spring, jakarta-nestjs, nestjs-spring.

Each `<framework>/applications/<app>/` directory is one deployable application:
a docker-compose project of several services in two or three languages plus its
infrastructure targets, carrying three to five planted weaknesses, benign
look-alike modules that expect silence, and a declared cross-service chain.
Each application is written in one API generation that its services share (an
older, still widely deployed line of both frameworks, or their current one; the
standalone bundles' READMEs name each line), and each graph's applications are
split across the generations its two frameworks have in common. An application's
build files and container images name the releases it targets.
Two CSV files per framework are the public ground truth:

- `<framework>/expectedresults-2026.11.22.csv` -- one row per flow and one per front door, columns
  `key,category,vulnerable,cwe,kind,truth,app_id,archetype,service,file,line`.
  For a flow, `kind` is `primary`, `planted` or `benign` and `truth` is
  `UNSANITIZED`, `SANITIZED_BROKEN` or `SANITIZED_EFFECTIVE`. For a front door,
  `kind` is `entry`, the key is `<app_id>:entry` and `truth` is `ENTRY_WEAKNESS`
  or `ENTRY_CONTROLLED`. `file` is relative to the framework suite root and
  `line` is the sink line (the first line of the entry service for a front door).
- `<framework>/expectedresults-chains-2026.11.22.csv` -- one row per chain edge per application, columns
  `app_id,archetype,edge_index,from_node,from_service,from_file,to_node,to_service,to_file,boundary,entry_service,entry_file,entry_cwe,entry_weakness_real,impact_cwe,chain_completes,planted_cwes`
  (`planted_cwes` joined with `;`; an application with no edge has one row with
  the edge columns empty).

Lines starting with `#` are comments in both files.

## Scan and score

1. Point your SAST tool at each `<framework>/applications/<app>/` directory
   (every application is its own project) and export one SARIF 2.1.0 file per
   framework suite. Artifact URIs must be relative to the framework suite root,
   i.e. `applications/<app>/services/<service>/<file>`, which is how the CSVs
   name them. A result may set `properties.testCaseKey` to the CSV key, and a
   `codeFlows` entry whose locations cross the services the tool followed is
   what earns layer-3 credit.
2. Score it against that framework's ground truth:

       python score_apps.py --flows express-django/expectedresults-2026.11.22.csv --chains express-django/expectedresults-chains-2026.11.22.csv --tool-sarif your_results.sarif

The scorer prints the triple (J1, A2, S3), reported side by side and never
averaged into one number:

- J1, flow judgment: Youden's J (sensitivity + specificity - 1) over every
  declared flow, so reporting everything scores 0 rather than 50%.
  Broken-sanitizer recall is reported beside it.
- A2, CWE identification, over the flows the tool got right at layer 1: the
  exact CWE scores 1.0, its hierarchy parent 0.5, anything else 0.
- S3, chain reconstruction, per application: the share of declared edges the
  tool's codeFlows recovered, doubled when the entry weakness is also named.
  Claiming a completed chain on an application whose control holds is a
  layer-3 false positive. Only counted for applications whose J1 clears the
  anti-gaming floor. Planted-CWE recall is reported beside it.

## Contents and integrity

- `benchproctor-manifest.json` -- version, per-framework counts (applications,
  flows by kind, front-door rows, chain edges), SHA-256 checksums.
- `score_apps.py` -- the stdlib scorer (no install).
- Every file is listed with its SHA-256 in the `SHASUMS256.txt` at the root of the release
  (`sha256sum -c SHASUMS256.txt` from there).

This bundle contains no answer key beyond the two public CSV files.
