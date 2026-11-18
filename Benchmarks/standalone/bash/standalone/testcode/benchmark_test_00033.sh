#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00033() {
  user_input="$QUERY_STRING"
  data="${user_input:-default}"
  mysql -e "SELECT * FROM users WHERE id = '$data'"
}

benchmark_test_00033 "$@"
