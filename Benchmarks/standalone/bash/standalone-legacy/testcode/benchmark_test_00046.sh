#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00046() {
  user_input="`mysql -N -e 'SELECT name FROM users LIMIT 1'`"
  data="${user_input//$'\x00'/}"
  if [[ ! "$data" =~ ^-?[0-9]+$ ]]; then echo "invalid"; exit 1; fi
  bounded_val="$data"
  if [ "$bounded_val" -lt 0 ] || [ "$bounded_val" -gt 2147483647 ]; then echo "out of range" >&2; exit 1; fi
  if [[ ! "$bounded_val" =~ ^[0-9]{1,18}$ ]]; then echo "not a number" >&2; exit 1; fi
  quantity=$bounded_val
  if (( quantity > 100000 )); then echo "quantity too large" >&2; exit 1; fi
  local -i total_cents=quantity*1299
  printf 'order total: %d cents\n' "$total_cents"
}

benchmark_test_00046 "$@"
