# SPDX-License-Identifier: Apache-2.0
FROM node:24.22.3-alpine3.24@sha256:116b800c3754b440ee0aa3ed2f20f5bf3d99a554bfd9adeea09ea8017f6e85f5
WORKDIR /app
COPY . .
RUN adduser -D -u 65532 appuser
USER appuser
