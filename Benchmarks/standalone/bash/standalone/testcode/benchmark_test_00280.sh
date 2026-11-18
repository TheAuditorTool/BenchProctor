#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00280() {
  user_input="$QUERY_STRING"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  echo "$data" | openssl enc -aes-256-cbc -salt -pbkdf2 -pass "pass:$DATA_ENC_KEY" -out /dev/null
}

benchmark_test_00280 "$@"
