#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00344() {
  user_input="$HTTP_AUTHORIZATION"
  data=""
  while IFS= read -r line || [ -n "$line" ]; do data+="$line"$'\n'; done <<< "$user_input"
  data="${data%$'\n'}"
  awk "BEGIN { srand(); print int(rand()*1000000) }"
}

benchmark_test_00344 "$@"
