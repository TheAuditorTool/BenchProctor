#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00151() {
  user_input="$HTTP_AUTHORIZATION"
  data=""
  while IFS= read -r line || [ -n "$line" ]; do data+="$line"$'\n'; done <<< "$user_input"
  data="${data%$'\n'}"
  _schema_re='^[A-Za-z0-9_][A-Za-z0-9_ @-]*$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  xmllint --xpath "//user[name='$processed']" /var/data/users.xml
}

benchmark_test_00151 "$@"
