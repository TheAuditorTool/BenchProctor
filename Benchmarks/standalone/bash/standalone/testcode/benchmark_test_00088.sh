#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00088() {
  user_input="$(cat /dev/stdin)"
  data=""
  while IFS= read -r line || [ -n "$line" ]; do data+="$line"$'\n'; done <<< "$user_input"
  data="${data%$'\n'}"
  if [[ ! "$data" =~ ^[0-9]{1,18}$ ]]; then echo "not a number" >&2; exit 1; fi
  quantity=$data
  local -i total_cents=quantity*1299
  printf 'order total: %d cents\n' "$total_cents"
}

benchmark_test_00088 "$@"
