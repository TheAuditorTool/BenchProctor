#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00350() {
  user_input="$HTTP_X_FORWARDED_FOR"
  data=""
  while IFS= read -r line || [ -n "$line" ]; do data+="$line"$'\n'; done <<< "$user_input"
  data="${data%$'\n'}"
  echo "$data" | openssl enc -aes-256-cbc -salt -pbkdf2 -pass "pass:$DATA_ENC_KEY" -out /dev/null
}

benchmark_test_00350 "$@"
