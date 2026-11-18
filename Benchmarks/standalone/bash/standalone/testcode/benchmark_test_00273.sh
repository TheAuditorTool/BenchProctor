#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00273() {
  user_input="$(sed -n 's/.*filename="\([^"]*\)".*/\1/p' | head -1)"
  data=$(printf "%s" "$user_input")
  _schema_re='^[A-Za-z0-9_][A-Za-z0-9_ @-]*$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  xmllint --xpath "//user[name='$processed']" /var/data/users.xml
}

benchmark_test_00273 "$@"
