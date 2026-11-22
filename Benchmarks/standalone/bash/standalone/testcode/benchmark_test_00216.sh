#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00216() {
  user_input="$(cat /dev/stdin)"
  data=""
  while IFS= read -r line || [ -n "$line" ]; do data+="$line"$'\n'; done <<< "$user_input"
  data="${data%$'\n'}"
  echo -n "$data" | md5sum
}

benchmark_test_00216 "$@"
