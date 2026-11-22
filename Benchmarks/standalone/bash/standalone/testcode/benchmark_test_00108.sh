#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00108() {
  user_input="$(jq -r '.value // empty' 2>/dev/null)"
  mapfile -t _mapped < <(printf "%s\n" "${user_input}")
  data="${_mapped[0]}"
  printf '%s' "$data" | openssl enc -aes-256-ctr -pbkdf2 -iter 600000 -pass env:DATA_ENC_KEY -out /var/app/run/record.enc
}

benchmark_test_00108 "$@"
