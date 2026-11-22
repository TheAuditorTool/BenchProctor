#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00010() {
  user_input="$(sed -n 's/.*filename="\([^"]*\)".*/\1/p' | head -1)"
  data="${user_input//$'\x00'/}"
  printf '%s' "$data" | openssl enc -aes-256-ctr -pbkdf2 -iter 600000 -pass env:DATA_ENC_KEY -out /var/app/run/record.enc
}

benchmark_test_00010 "$@"
