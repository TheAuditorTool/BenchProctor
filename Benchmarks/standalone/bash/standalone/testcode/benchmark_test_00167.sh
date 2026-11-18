#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00167() {
  user_input="$(tr '&' '\n' | grep '^field=' | cut -d= -f2-)"
  data=$(printf "%b" "${user_input//%/\\x}")
  if [[ ! "$data" =~ ^-?[0-9]+$ ]]; then echo "not a number" >&2; exit 1; fi
  requested=$data
  alloc_size=$((requested + 1))
  echo "alloc:$alloc_size"
}

benchmark_test_00167 "$@"
