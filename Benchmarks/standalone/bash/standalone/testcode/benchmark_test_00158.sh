#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00158() {
  user_input="$(jq -r '.variables.input // empty' 2>/dev/null)"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  if [[ ! "$data" =~ ^-?[0-9]+$ ]]; then echo "not a number" >&2; exit 1; fi
  requested=$data
  alloc_size=$((requested + 1))
  echo "alloc:$alloc_size"
}

benchmark_test_00158 "$@"
