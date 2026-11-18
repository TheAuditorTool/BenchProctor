#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00231() {
  user_input="$(jq -r '.value // empty' 2>/dev/null)"
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$user_input" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$user_input"
  mysql -e "SELECT * FROM users ORDER BY $processed"
}

benchmark_test_00231 "$@"
