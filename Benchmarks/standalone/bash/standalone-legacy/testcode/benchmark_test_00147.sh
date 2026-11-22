#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00147() {
  user_input="`mysql -N -e 'SELECT name FROM users LIMIT 1'`"
  data=`echo "$user_input" | xxd -r -p 2>/dev/null || echo ""`
  psql "$DATABASE_URL" -qAt -c "PREPARE user_lookup AS SELECT * FROM users WHERE id = '$data'; EXECUTE user_lookup;"
}

benchmark_test_00147 "$@"
