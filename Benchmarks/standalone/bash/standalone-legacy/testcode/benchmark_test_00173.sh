#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00173() {
  user_input="`jq -r '.value // empty' 2>/dev/null`"
  data=`echo "$user_input" | jq -r '.value // empty' 2>/dev/null || echo ""`
  if [[ ! "$data" =~ ^[0-9]{1,18}$ ]]; then echo "not a number" >&2; exit 1; fi
  quantity=$data
  local -i total_cents=quantity*1299
  printf 'order total: %d cents\n' "$total_cents"
}

benchmark_test_00173 "$@"
