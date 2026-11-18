#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00181() {
  user_input="$(jq -r '.value // empty' 2>/dev/null)"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  echo "$data" | openssl enc -aes-256-cbc -salt -pbkdf2 -pass "pass:$DATA_ENC_KEY" -out /dev/null
}

benchmark_test_00181 "$@"
