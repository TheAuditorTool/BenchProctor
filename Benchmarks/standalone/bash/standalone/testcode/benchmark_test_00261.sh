#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00261() {
  user_input="$USER_COMMENT"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  echo "$data" | xmllint --nonet - > /dev/null 2>&1
}

benchmark_test_00261 "$@"
