#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00332() {
  user_input="$HTTP_COOKIE"
  data=""
  while IFS= read -r line || [ -n "$line" ]; do data+="$line"$'\n'; done <<< "$user_input"
  data="${data%$'\n'}"
  checked_path="/var/app/data/$(basename -- "$data")"
  rm -f "$checked_path"
}

benchmark_test_00332 "$@"
