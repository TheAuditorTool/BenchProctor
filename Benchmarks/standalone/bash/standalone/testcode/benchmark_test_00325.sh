#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00325() {
  user_input="$HTTP_AUTHORIZATION"
  data=$(printf "%s" "$user_input")
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  mysql -e "SELECT * FROM users ORDER BY $processed"
}

benchmark_test_00325 "$@"
