#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00267() {
  user_input="$1"
  data=""
  while IFS= read -r line || [ -n "$line" ]; do data+="$line"$'\n'; done <<< "$user_input"
  data="${data%$'\n'}"
  cat "/var/app/data/$data"
}

benchmark_test_00267 "$@"
