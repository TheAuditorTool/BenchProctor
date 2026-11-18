#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00376() {
  user_input="$HTTP_ORIGIN"
  data=""
  while IFS= read -r line || [ -n "$line" ]; do data+="$line"$'\n'; done <<< "$user_input"
  data="${data%$'\n'}"
  echo -n "$data" | sha256sum
}

benchmark_test_00376 "$@"
