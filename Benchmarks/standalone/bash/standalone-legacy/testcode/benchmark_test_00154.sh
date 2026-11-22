#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00154() {
  user_input="`sed -n '/^\r*$/{n;s/\r$//;p;q}'`"
  data=""
  while IFS= read -r line || [ -n "$line" ]; do data+="$line"$'\n'; done <<< "$user_input"
  data="${data%$'\n'}"
  echo "$data" | xmllint --nonet - > /dev/null 2>&1
}

benchmark_test_00154 "$@"
