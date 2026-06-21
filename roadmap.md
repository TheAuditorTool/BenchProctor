# Roadmap

BenchProctor publishes a language only once its labels pass our full gate suite. Standalone
single-file corpora first; the goal is never to ship labels we can't defend.

## Shipping now

- **Java** — Spring, Jakarta EE — standalone, all supported CWE categories.
- **Python** — Flask, Django, FastAPI — standalone, all supported CWE categories.

Each ships in three sizes:

- `quicktest` (~10k tests/language) — the most prevalent CWEs at 25 vulnerable + 25 safe per type.
- `normal` (~40k) — ~all supported CWEs at 50 + 50 per type. The headline scoreable corpus.
- `enterprise` (all CWEs, deepest sampling) — for tighter confidence intervals.

## Next — in order, as each clears the same gate suite

- Go (net/http, Gin)
- Rust (Actix-web, Axum)
- TypeScript (NestJS, Express)
- JavaScript (Express, Koa)
- PHP (Laravel, Symfony)
- Ruby (Rails, Sinatra)
- Bash

## Later

- Cross-file CWE chains — a weakness threaded across modules and functions so smaller findings
  compound into a larger compromise.
- Polyglot microservice scenarios — taint that crosses language and process boundaries (HTTP, gRPC,
  subprocess, environment variables, message queues).
- Adversarial / SAST-evasion cases.
- An all-hard difficulty mode for the enterprise tier.

## How releases work

Corpora are versioned and released quarterly. Each release rotates a fixed seed: the emitted code
changes, while every scoring-relevant invariant — CWE identity, difficulty mix, 50/50 balance,
language and framework coverage — stays constant. Last quarter's score stays comparable, and a model
trained on last quarter's files learns nothing about this quarter's.
