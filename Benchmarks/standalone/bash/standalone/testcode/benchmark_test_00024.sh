#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00024() {
  user_input="$QUERY_STRING"
  data=$(printf "%b" "${user_input//%/\\x}")
  mysql -e "SELECT * FROM users WHERE id = '$data'"
}

benchmark_test_00024 "$@"
