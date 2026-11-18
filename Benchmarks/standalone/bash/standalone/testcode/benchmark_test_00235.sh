#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00235() {
  user_input="$QUERY_STRING"
  mysql -e "SELECT * FROM users WHERE id = '$user_input'"
}

benchmark_test_00235 "$@"
