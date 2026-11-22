#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00092() {
  user_input="`jq -r '.value // empty' 2>/dev/null`"
  data=""
  while IFS= read -r line || [ -n "$line" ]; do data+="$line"$'\n'; done <<< "$user_input"
  data="${data%$'\n'}"
  echo "$data" | xmllint --nonet - > /dev/null 2>&1
}

benchmark_test_00092 "$@"
