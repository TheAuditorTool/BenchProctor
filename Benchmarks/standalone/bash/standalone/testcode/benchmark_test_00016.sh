#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00016() {
  user_input="$HTTP_COOKIE"
  data=$(echo "$user_input" | xxd -r -p 2>/dev/null || echo "")
  echo "$data" | openssl enc -aes-256-cbc -salt -pbkdf2 -pass "pass:$DATA_ENC_KEY" -out /dev/null
}

benchmark_test_00016 "$@"
