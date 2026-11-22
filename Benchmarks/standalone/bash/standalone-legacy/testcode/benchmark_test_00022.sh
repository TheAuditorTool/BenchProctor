#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00022() {
  user_input="`mysql -N -e 'SELECT bio FROM profiles LIMIT 1'`"
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$user_input" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$user_input"
  psql "$DATABASE_URL" -qAt -c "PREPARE user_lookup AS SELECT * FROM users ORDER BY $processed; EXECUTE user_lookup;"
}

benchmark_test_00022 "$@"
