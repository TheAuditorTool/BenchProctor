#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00030() {
  user_input="$QUERY_STRING"
  data="${user_input:-default}"
  printf '%s' "$data" | openssl enc -aes-256-ecb -pbkdf2 -iter 600000 -pass env:DATA_ENC_KEY -out /var/app/run/record.enc
}

benchmark_test_00030 "$@"
