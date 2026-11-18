#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00389() {
  user_input="$(mysql -N -e 'SELECT name FROM users LIMIT 1')"
  data=$(echo "$user_input" | xxd -r -p 2>/dev/null || echo "")
  echo "$data" | openssl enc -aes-256-cbc -salt -pbkdf2 -pass "pass:$DATA_ENC_KEY" -out /dev/null
}

benchmark_test_00389 "$@"
