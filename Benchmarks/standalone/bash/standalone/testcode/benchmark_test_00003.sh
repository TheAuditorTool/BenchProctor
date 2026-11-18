#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00003() {
  user_input="$(mysql -N -e 'SELECT name FROM users LIMIT 1')"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=$(normalize "$user_input")
  echo -n "$data" | sha256sum
}

benchmark_test_00003 "$@"
