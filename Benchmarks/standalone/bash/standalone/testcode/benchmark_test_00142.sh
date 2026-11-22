#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00142() {
  user_input="$(jq -r '.value // empty' 2>/dev/null)"
  data=""
  while IFS= read -r line || [ -n "$line" ]; do data+="$line"$'\n'; done <<< "$user_input"
  data="${data%$'\n'}"
  echo -n "$data" | md5sum
}

benchmark_test_00142 "$@"
