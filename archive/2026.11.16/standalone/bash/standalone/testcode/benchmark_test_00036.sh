#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00036() {
  user_input="$HTTP_HOST"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=$(normalize "$user_input")
  echo "$data" | openssl enc -aes-256-cbc -salt -pbkdf2 -pass "pass:$DATA_ENC_KEY" -out /dev/null
}

benchmark_test_00036 "$@"
