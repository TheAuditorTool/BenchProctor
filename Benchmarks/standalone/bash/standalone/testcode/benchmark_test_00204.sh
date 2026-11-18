#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00204() {
  user_input="$PATH_INFO"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  mysql -e "SELECT * FROM users ORDER BY $processed"
}

benchmark_test_00204 "$@"
