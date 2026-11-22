#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00168() {
  user_input="$(mysql -N -e 'SELECT name FROM users LIMIT 1')"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=$(normalize "$user_input")
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  xmlstarlet sel -t -v "//user[name='$processed']/email" /var/data/users.xml
}

benchmark_test_00168 "$@"
