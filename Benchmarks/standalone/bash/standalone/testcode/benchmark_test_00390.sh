#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00390() {
  user_input="$QUERY_STRING"
  data=""
  while IFS= read -r line || [ -n "$line" ]; do data+="$line"$'\n'; done <<< "$user_input"
  data="${data%$'\n'}"
  _bool_re='^(true|false|1|0)$'
  if [[ ! "$data" =~ $_bool_re ]]; then echo "invalid bool" >&2; exit 1; fi
  parsed_bool="$data"
  xmllint --xpath "//user[name='$parsed_bool']" /var/data/users.xml
}

benchmark_test_00390 "$@"
