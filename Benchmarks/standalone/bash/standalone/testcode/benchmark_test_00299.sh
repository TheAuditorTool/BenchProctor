#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00299() {
  user_input="$(sed -n 's/.*filename="\([^"]*\)".*/\1/p' | head -1)"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=$(normalize "$user_input")
  mysql -e "SELECT * FROM users WHERE id = '$data'"
}

benchmark_test_00299 "$@"
