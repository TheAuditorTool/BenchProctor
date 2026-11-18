#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00022() {
  user_input="$HTTP_AUTHORIZATION"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=$(make_reader)
  if [[ ! "$data" =~ ^-?[0-9]+$ ]]; then echo "not a number" >&2; exit 1; fi
  requested=$data
  alloc_size=$((requested + 1))
  echo "alloc:$alloc_size"
}

benchmark_test_00022 "$@"
