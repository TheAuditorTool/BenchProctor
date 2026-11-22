#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00032() {
  user_input="`jq -r '.variables.input // empty' 2>/dev/null`"
  data=`printf "%s" "${user_input}" | tr -s " "`
  printf '%s' "$data" | openssl enc -aes-256-ctr -pbkdf2 -iter 600000 -pass env:DATA_ENC_KEY -out /var/app/run/record.enc
}

benchmark_test_00032 "$@"
