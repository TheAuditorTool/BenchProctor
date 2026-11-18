#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00012() {
  user_input="$USER_COMMENT"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=$(normalize "$user_input")
  if [[ ! "$data" =~ ^-?[0-9]+$ ]]; then echo "not a number" >&2; exit 1; fi
  requested=$data
  alloc_size=$((requested + 1))
  echo "alloc:$alloc_size"
}

benchmark_test_00012 "$@"
