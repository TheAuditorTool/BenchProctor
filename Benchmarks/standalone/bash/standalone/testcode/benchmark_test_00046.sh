#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00046() {
  user_input="$(sed -n 's/.*filename="\([^"]*\)".*/\1/p' | head -1)"
  printf -v data "%s" "${user_input}"
  if [[ ! "$data" =~ ^-?[0-9]+$ ]]; then echo "not a number" >&2; exit 1; fi
  requested=$data
  alloc_size=$((requested + 1))
  echo "alloc:$alloc_size"
}

benchmark_test_00046 "$@"
