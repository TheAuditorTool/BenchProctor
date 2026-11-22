# SPDX-License-Identifier: Apache-2.0
FROM debian:13.6-slim@sha256:d7e12182ce18b85b93007c1dedf31f2d29e01ccf3182cc4017c709b6259bc132
WORKDIR /app
COPY . .
RUN useradd -u 65532 -m appuser
USER appuser
