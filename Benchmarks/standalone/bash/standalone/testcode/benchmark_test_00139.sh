#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00139() {
  user_input="$HTTP_USER_AGENT"
  echo "$user_input" | openssl enc -aes-256-cbc -salt -pbkdf2 -pass "pass:$DATA_ENC_KEY" -out /dev/null
}

benchmark_test_00139 "$@"
