#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00373() {
  user_input="$USER_COMMENT"
  data="${user_input:-default}"
  echo "$data" | openssl enc -aes-256-cbc -salt -pbkdf2 -pass "pass:$DATA_ENC_KEY" -out /dev/null
}

benchmark_test_00373 "$@"
