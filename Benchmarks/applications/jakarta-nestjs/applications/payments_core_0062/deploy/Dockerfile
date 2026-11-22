# SPDX-License-Identifier: Apache-2.0
FROM python:3.14.8-slim-trixie@sha256:fbecd461fc72d21b2143c6eaba25143738079154a6d0ea3da3aec724f50eed4a
WORKDIR /app
COPY . .
RUN useradd -u 65532 -m appuser
USER appuser
