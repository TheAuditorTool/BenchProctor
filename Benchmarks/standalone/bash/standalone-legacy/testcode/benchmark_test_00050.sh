#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00050() {
  user_input="`tr '&' '\n' | grep '^field=' | cut -d= -f2-`"
  data=""
  while IFS= read -r line || [ -n "$line" ]; do data+="$line"$'\n'; done <<< "$user_input"
  data="${data%$'\n'}"
  printf '%s' "$data" | xmllint --stream --nonet -
}

benchmark_test_00050 "$@"
