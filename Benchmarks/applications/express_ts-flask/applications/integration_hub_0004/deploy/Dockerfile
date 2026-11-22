# SPDX-License-Identifier: Apache-2.0
FROM alpine:3.24.2@sha256:294b683cb724975bec92580e1e685676bd4b50bda910ddb8c51d4cabeaec77e6
WORKDIR /app
COPY . .
RUN adduser -D -u 65532 appuser
USER appuser
