#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00175() {
  user_input="$HTTP_AUTHORIZATION"
  data=`printf "%s" "${user_input}" | tr -s " "`
  if [[ ! "$data" =~ ^-?[0-9]+$ ]]; then echo "invalid"; exit 1; fi
  bounded_val="$data"
  if [ "$bounded_val" -lt 0 ] || [ "$bounded_val" -gt 2147483647 ]; then echo "out of range" >&2; exit 1; fi
  if [[ ! "$bounded_val" =~ ^-?[0-9]+$ ]]; then echo "invalid" >&2; exit 1; fi
  requested=$bounded_val
  if [ "${#requested}" -gt 10 ] || [ "$requested" -lt 0 ] || [ "$requested" -gt 2147483646 ]; then echo "out of range" >&2; exit 1; fi
  alloc_size=$((requested + 1))
  echo "alloc:$alloc_size"
}

benchmark_test_00175 "$@"
