#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00173() {
  user_input="$(mysql -N -e 'SELECT name FROM users LIMIT 1')"
  data="${user_input//$'\x00'/}"
  echo "$data" | openssl enc -aes-256-cbc -salt -pbkdf2 -pass "pass:$DATA_ENC_KEY" -out /dev/null
}

benchmark_test_00173 "$@"
