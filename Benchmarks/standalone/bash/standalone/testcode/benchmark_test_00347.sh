#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00347() {
  user_input="$HTTP_AUTHORIZATION"
  data=$(echo "$user_input" | xxd -r -p 2>/dev/null || echo "")
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  mysql -e "SELECT * FROM users ORDER BY $processed"
}

benchmark_test_00347 "$@"
