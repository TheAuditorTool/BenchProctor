#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00143() {
  user_input="$(tr '&' '\n' | grep '^field=' | cut -d= -f2-)"
  data=$(printf "%s" "$user_input")
  echo "$data" | openssl enc -aes-256-cbc -salt -pbkdf2 -pass "pass:$DATA_ENC_KEY" -out /dev/null
}

benchmark_test_00143 "$@"
