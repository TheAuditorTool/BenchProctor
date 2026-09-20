# Roadmap

BenchProctor publishes only what passes our full gate suite. We won't ship labels we can't defend.
Standalone single-file corpora came first. The next release adds depth on two fronts at once: a far
larger, fully unlocked framework surface for standalone, and a new application shape whose findings
cross files, languages, and processes.

## Shipping now

### Standalone, all 11 languages plus Solidity

Single-file finding cases in `quicktest`, `normal`, and `enterprise` sizes, each cleared through the
same gate suite (compile or parse, real source-to-sink taint on every vulnerable case, a genuinely
effective sanitizer on every safe twin, and a verified sink line). The framework surface is now the
full frozen catalogue: 64 code-language lanes plus 21 infrastructure substrates, drawing on 118
pinnable third-party libraries.

- **Python**: Flask, Django, FastAPI, DRF, aiohttp, GraphQL, argparse, Typer, Click, Celery, serverless
- **JavaScript**: Express, Koa, Fastify, GraphQL, serverless
- **TypeScript**: NestJS, Express, Fastify, Hono, Next.js, Angular, React, Vue, Svelte, SvelteKit, GraphQL, serverless
- **Go**: net/http, Gin, Echo, Fiber, Chi, Gorilla, GraphQL, Cobra, serverless, standalone
- **Java**: Spring, Jakarta EE, Quarkus, GraphQL, picocli, serverless
- **Ruby**: Rails, Sinatra, GraphQL
- **PHP**: Laravel, Symfony, Symfony Console, GraphQL
- **Rust**: Actix-web, Axum, Rocket, GraphQL, clap, standalone
- **C**: standalone, host, kernel
- **C++**: standalone, cpp-httplib
- **Bash**: standalone
- **Solidity**: contract

Earlier releases locked JavaScript to Koa and TypeScript to Express. Both now draw from the full
modern Node surface above. Every web language also ships a GraphQL resolver lane, and most gain
command-line and serverless or worker lanes.

Sizes:

- `quicktest`: the most prevalent classes (CWE Top 25 2024 + OWASP Top 10 2021), 50 vulnerable +
  50 safe per category.
- `normal`: all supported categories, up to 100 + 100 per category. The headline scoreable corpus.
- `enterprise`: all supported categories, up to 250 + 250 per category, deepest sampling.

### Application projects

Small, realistic, buildable polyglot projects: 2-3 application-tier languages plus 1-2 cloud or
infrastructure targets, several planted CWEs per project, and, where the archetype allows, a compound
chain that escalates across services with a defensive gate on an upstream link so the safe variant
closes the chain. Each project builds under its native toolchains as a unit and passes a Docker
runtime gate before release. The shape is scored as a triple, flow judgment, CWE identification, and
chain reconstruction, reported side by side and never averaged. See the scoring section of
[README.md](README.md).

This shape subsumes the earlier separate axes of cross-file CWE chains and polyglot microservice
scenarios: both are now properties of an application rather than standalone deliverables.

## Ahead

Status reflects where each area stands today, not a target date. Nothing publishes until it clears
its own gate.

- **Adversarial / SAST-evasion cases**: files that use homoglyphs, right-to-left overrides, null
  bytes, encoding tricks, and other concealment techniques to hide an otherwise real vulnerability
  from a naive scanner. Generating and passing basic checks; still expanding the technique set and
  finishing their own QC.

- **Standalone infrastructure-as-code config-state coverage**: the substrates already ship as
  deploy-time artifacts inside applications. Bringing the config-state weakness classes (public
  exposure, missing encryption, permissive IAM, unpinned dependencies, missing security headers,
  disabled audit logging) up to the same standalone gate bar broadens single-file IaC coverage.

- **An all-hard difficulty mode** for the enterprise tier.

## How releases work

Corpora are versioned by date (`YYYY.MM.DD`) and released periodically. Each release rotates a fixed
seed: the emitted code changes, while every scoring-relevant invariant (CWE identity, difficulty mix,
50/50 balance, language and framework coverage) stays constant. Last release's score stays
comparable, and a model trained on last release's files learns nothing about this one's.
