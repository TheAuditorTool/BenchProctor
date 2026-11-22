#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00063() {
  user_input="$1"
  data=`printf "%s" "${user_input}" | tr -s " "`
  sqlite3 /var/app/data/app.db "SELECT * FROM users WHERE id = '$data'"
}

benchmark_test_00063 "$@"
