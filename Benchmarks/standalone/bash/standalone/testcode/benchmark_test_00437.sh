#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00437() {
  user_input="$(mysql -N -e 'SELECT name FROM users LIMIT 1')"
  data=$(printf "%s" "${user_input}" | tr -s " ")
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  xmllint --xpath "//user[name='$processed']" /var/data/users.xml
}

benchmark_test_00437 "$@"
