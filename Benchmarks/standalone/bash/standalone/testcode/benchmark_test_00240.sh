#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00240() {
  user_input="$(mysql -N -e 'SELECT name FROM users LIMIT 1')"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=$(normalize "$user_input")
  if [[ ! "$data" =~ ^-?[0-9]+$ ]]; then echo "not a number" >&2; exit 1; fi
  requested=$data
  alloc_size=$((requested + 1))
  echo "alloc:$alloc_size"
}

benchmark_test_00240 "$@"
