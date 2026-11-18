#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00229() {
  user_input="$(jq -r '.variables.input // empty' 2>/dev/null)"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=$(normalize "$user_input")
  _schema_re='^[A-Za-z0-9_][A-Za-z0-9_ @-]*$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  xmllint --xpath "//user[name='$processed']" /var/data/users.xml
}

benchmark_test_00229 "$@"
