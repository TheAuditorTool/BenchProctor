#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00219() {
  user_input="$(sed -n '/^\r*$/{n;s/\r$//;p;q}')"
  if [[ ! "$user_input" =~ ^-?[0-9]+$ ]]; then echo "invalid"; exit 1; fi
  bounded_val="$user_input"
  if [ "$bounded_val" -lt 0 ] || [ "$bounded_val" -gt 2147483647 ]; then echo "overflow"; exit 1; fi
  if [[ ! "$bounded_val" =~ ^-?[0-9]+$ ]]; then echo "invalid" >&2; exit 1; fi
  requested=$bounded_val
  if [ "$requested" -lt 0 ] || [ "$requested" -gt 2147483646 ]; then echo "overflow" >&2; exit 1; fi
  alloc_size=$((requested + 1))
  echo "alloc:$alloc_size"
}

benchmark_test_00219 "$@"
