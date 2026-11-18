#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00237() {
  user_input="$(sed -n 's/.*filename="\([^"]*\)".*/\1/p' | head -1)"
  data=$(printf "%s" "${user_input}" | tr -s " ")
  mysql -e "SELECT * FROM users WHERE id = '$data'"
}

benchmark_test_00237 "$@"
