#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00079() {
  user_input="$PATH_INFO"
  data=""
  while IFS= read -r line || [ -n "$line" ]; do data+="$line"$'\n'; done <<< "$user_input"
  data="${data%$'\n'}"
  echo -n "$data" | md5sum
}

benchmark_test_00079 "$@"
