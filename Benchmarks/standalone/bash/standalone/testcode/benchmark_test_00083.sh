#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00083() {
  user_input="$(cat /dev/stdin)"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=$(normalize "$user_input")
  mysql -e "SELECT * FROM users WHERE id = '$data'"
}

benchmark_test_00083 "$@"
