#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00432() {
  user_input="$(jq -r '.variables.input // empty' 2>/dev/null)"
  data="${user_input//$'\x00'/}"
  echo "$data" | openssl enc -aes-256-cbc -salt -pbkdf2 -pass "pass:$DATA_ENC_KEY" -out /dev/null
}

benchmark_test_00432 "$@"
