#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00068() {
  user_input="`tr '&' '\n' | grep '^field=' | cut -d= -f2-`"
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$user_input" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$user_input"
  sqlite3 /var/app/data/app.db "SELECT * FROM users ORDER BY $processed"
}

benchmark_test_00068 "$@"
