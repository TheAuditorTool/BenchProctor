#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00184() {
  user_input="$HTTP_X_CUSTOM_HEADER"
  data=""
  while IFS= read -r line || [ -n "$line" ]; do data+="$line"$'\n'; done <<< "$user_input"
  data="${data%$'\n'}"
  curl -s --max-time 10 -- "$data"
}

benchmark_test_00184 "$@"
