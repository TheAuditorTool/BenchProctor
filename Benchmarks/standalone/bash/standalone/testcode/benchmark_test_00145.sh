#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00145() {
  user_input="$(cat /etc/app/config)"
  data=$(echo "$user_input" | jq -r '.value // empty' 2>/dev/null || echo "")
  psql "$DATABASE_URL" -qAt -c "PREPARE user_lookup AS SELECT * FROM users WHERE id = '$data'; EXECUTE user_lookup;"
}

benchmark_test_00145 "$@"
