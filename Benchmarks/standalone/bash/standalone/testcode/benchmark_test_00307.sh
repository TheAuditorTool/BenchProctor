#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00307() {
  user_input="$1"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=$(make_reader)
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  mysql -e "SELECT * FROM users ORDER BY $processed"
}

benchmark_test_00307 "$@"
