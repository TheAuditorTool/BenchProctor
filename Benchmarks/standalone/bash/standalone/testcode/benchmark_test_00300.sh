#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00300() {
  user_input="$(jq -r '.variables.input // empty' 2>/dev/null)"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=$(normalize "$user_input")
  echo "$data" | openssl enc -aes-256-cbc -salt -pbkdf2 -pass "pass:$DATA_ENC_KEY" -out /dev/null
}

benchmark_test_00300 "$@"
