#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00068() {
  user_input="$(jq -r '.value // empty' 2>/dev/null)"
  printf -v data "%s" "${user_input}"
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  psql "$DATABASE_URL" -qAt -c "PREPARE user_lookup AS SELECT * FROM users ORDER BY $processed; EXECUTE user_lookup;"
}

benchmark_test_00068 "$@"
