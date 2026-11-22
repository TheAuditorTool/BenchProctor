#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00022() {
  user_input="$(mysql -N -e 'SELECT bio FROM profiles LIMIT 1')"
  data=$(printf "%s" "${user_input}" | tr -s " ")
  psql "$DATABASE_URL" -qAt -c "PREPARE user_lookup AS SELECT * FROM users WHERE id = '$data'; EXECUTE user_lookup;"
}

benchmark_test_00022 "$@"
