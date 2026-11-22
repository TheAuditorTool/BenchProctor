#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00217() {
  user_input="`mysql -N -e 'SELECT name FROM users LIMIT 1'`"
  data="${user_input:-default}"
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  sqlite3 /var/app/data/app.db "SELECT * FROM users ORDER BY $processed"
}

benchmark_test_00217 "$@"
