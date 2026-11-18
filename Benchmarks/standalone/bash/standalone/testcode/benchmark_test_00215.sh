#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00215() {
  user_input="$QUERY_STRING"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  awk "BEGIN { srand(); print int(rand()*1000000) }"
}

benchmark_test_00215 "$@"
