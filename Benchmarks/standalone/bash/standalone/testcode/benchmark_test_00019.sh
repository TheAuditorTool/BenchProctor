#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00019() {
  user_input="$(jq -r '.value // empty' 2>/dev/null)"
  data=$(printf "%s" "${user_input}" | tr -s " ")
  mysql -e "SELECT * FROM users WHERE id = '$data'"
}

benchmark_test_00019 "$@"
