# Roadmap

BenchProctor publishes only what passes our full gate suite. We won't ship labels we can't defend.
Standalone single-file corpora came first; the next axis is depth: findings that cross files,
languages, and processes.

## Shipping now: standalone, all 11 languages

Every language below ships in `quicktest`, `normal`, and `enterprise` sizes, each cleared through
the same gate suite (compile/parse, real source-to-sink taint on every vulnerable case, a genuinely
effective sanitizer on every safe twin, and a verified sink line).

- **Java**: Spring, Jakarta EE
- **Python**: Flask, Django, FastAPI
- **Go**: Gin, net/http
- **Rust**: Actix-web, Axum
- **TypeScript**: NestJS, Express
- **JavaScript**: Express, Koa
- **PHP**: Laravel, Symfony
- **Ruby**: Rails, Sinatra
- **C++**: cpp-httplib, standalone
- **C**: standalone
- **Bash**: standalone

Sizes:

- `quicktest`: the most prevalent classes (CWE Top 25 2024 + OWASP Top 10 2021), 50 vulnerable +
  50 safe per category.
- `normal`: all supported categories, up to 100 + 100 per category. The headline scoreable corpus.
- `enterprise`: all supported categories, up to 250 + 250 per category, deepest sampling.

## In active development

These shapes already generate and pass the full internal gate suite across all 11 languages; what
remains before a public release is coverage breadth and final packaging. Status reflects where each
stands today, not a target date.

- **Cross-file CWE chains**: a single weakness threaded across modules and functions so smaller
  findings compound into a larger compromise, with a defensive gate placed on an upstream link so
  the safe twin closes the chain before it reaches the sink. *Building green across all 11
  languages; a small set of language/topology combinations narrow out by design where a language
  cannot express a given upstream defense. Finalizing coverage before release.*

- **Polyglot microservice scenarios**: taint that crosses language and process boundaries: one
  service reads untrusted input and hands it to another over HTTP, a message queue, a subprocess,
  or an environment variable, where the sink lives in a different language. Two-hop and three-hop
  topologies. *Building green across the language matrix; hardening the cross-boundary contracts
  before release.*

- **Adversarial / SAST-evasion cases**: hand-authored files that use homoglyphs, right-to-left
  overrides, null bytes, and encoding tricks to hide an otherwise real vulnerability from a naive
  scanner. *Generating and passing basic checks; still ironing out the quirks and expanding the
  technique set.*

## Later

- Infrastructure-as-code and config targets already modeled in the platform (Terraform/HCL,
  CloudFormation, Kubernetes manifests, Dockerfiles, GitHub Actions, GitLab CI, CDK, Pulumi),
  brought up to the same gate bar and released.
- An all-hard difficulty mode for the enterprise tier.

## How releases work

Corpora are versioned and released periodically. Each release rotates a fixed seed: the emitted code
changes, while every scoring-relevant invariant (CWE identity, difficulty mix, 50/50 balance,
language and framework coverage) stays constant. Last release's score stays comparable, and a model
trained on last release's files learns nothing about this one's.
