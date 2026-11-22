# SPDX-License-Identifier: Apache-2.0
FROM ubuntu:resolute-20261006@sha256:c098726dd9b9733f3e885f8de0ef375206a311b0a317eadc40d347b1115fb944
WORKDIR /app
COPY . .
RUN useradd -u 65532 -m appuser
USER appuser
