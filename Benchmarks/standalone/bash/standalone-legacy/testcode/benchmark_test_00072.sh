#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00072() {
  user_input="$HTTP_AUTHORIZATION"
  data=`printf "%s" "$user_input"`
  if [[ ! "$data" =~ ^-?[0-9]+$ ]]; then echo "not a number" >&2; exit 1; fi
  requested=$data
  alloc_size=$((requested + 1))
  echo "alloc:$alloc_size"
}

benchmark_test_00072 "$@"
