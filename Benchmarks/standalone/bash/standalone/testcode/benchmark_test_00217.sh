#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00217() {
  user_input="$HTTP_COOKIE"
  data=$(printf "%s" "${user_input}" | tr -s " ")
  _schema_re='^[a-zA-Z0-9#._-]+$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  sqlite3 /var/app/data/app.db "SELECT * FROM users WHERE id = '$processed'"
}

benchmark_test_00217 "$@"
