#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00168() {
  user_input="`mysql -N -e 'SELECT name FROM users LIMIT 1'`"
  _first_line() { IFS= read -r _line; printf '%s' "$_line"; }
  data=`printf "%s\n" "${user_input}" | _first_line`
  _schema_re='^[A-Za-z0-9_][A-Za-z0-9_ @-]*$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  xmlstarlet sel -t -v "//user[name='$processed']/email" /var/data/users.xml
}

benchmark_test_00168 "$@"
