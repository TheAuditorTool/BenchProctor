#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00212() {
  user_input="$HTTP_COOKIE"
  echo "$user_input" | openssl enc -aes-256-cbc -salt -pbkdf2 -pass "pass:$DATA_ENC_KEY" -out /dev/null
}

benchmark_test_00212 "$@"
