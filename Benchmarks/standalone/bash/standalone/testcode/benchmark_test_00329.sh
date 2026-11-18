#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00329() {
  user_input="$HTTP_X_CUSTOM_HEADER"
  data=$(echo "$user_input" | xxd -r -p 2>/dev/null || echo "")
  _bool_re='^(true|false|1|0)$'
  if [[ ! "$data" =~ $_bool_re ]]; then echo "invalid bool" >&2; exit 1; fi
  parsed_bool="$data"
  xmllint --xpath "//user[name='$parsed_bool']" /var/data/users.xml
}

benchmark_test_00329 "$@"
