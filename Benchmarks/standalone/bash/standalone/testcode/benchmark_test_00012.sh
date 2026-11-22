#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00012() {
  user_input="$HTTP_ORIGIN"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  printf '%s' "$data" | openssl enc -aes-256-ctr -pbkdf2 -iter 600000 -pass env:DATA_ENC_KEY -out /var/app/run/record.enc
}

benchmark_test_00012 "$@"
