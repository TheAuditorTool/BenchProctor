#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00067() {
  user_input="$HTTP_X_CUSTOM_HEADER"
  data=$(printf "%s" "${user_input}" | tr -s " ")
  if [[ ! "$data" =~ ^-?[0-9]+$ ]]; then echo "not a number" >&2; exit 1; fi
  requested=$data
  alloc_size=$((requested + 1))
  echo "alloc:$alloc_size"
}

benchmark_test_00067 "$@"
