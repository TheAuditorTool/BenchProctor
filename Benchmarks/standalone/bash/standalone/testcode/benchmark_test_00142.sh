#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00142() {
  user_input="$(cat /dev/stdin)"
  data=$(printf "%b" "$user_input")
  mysql -e "SELECT * FROM users WHERE id = '$data'"
}

benchmark_test_00142 "$@"
