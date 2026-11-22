#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00166() {
  user_input="$QUERY_STRING"
  data=$(printf "%b" "${user_input//%/\\x}")
  sqlite3 /var/app/data/app.db "SELECT * FROM users WHERE id = '$data'"
}

benchmark_test_00166 "$@"
