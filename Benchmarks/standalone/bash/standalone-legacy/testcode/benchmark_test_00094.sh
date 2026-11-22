#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00094() {
  user_input="$HTTP_REFERER"
  data=""
  while IFS= read -r line || [ -n "$line" ]; do data+="$line"$'\n'; done <<< "$user_input"
  data="${data%$'\n'}"
  printf '%s' "$data" | openssl enc -aes-256-ecb -pbkdf2 -iter 600000 -pass env:DATA_ENC_KEY -out /var/app/run/record.enc
}

benchmark_test_00094 "$@"
