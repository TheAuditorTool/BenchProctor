#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00024() {
  user_input="$HTTP_X_FORWARDED_FOR"
  _bool_re='^(true|false|1|0)$'
  if [[ ! "$user_input" =~ $_bool_re ]]; then echo "invalid bool" >&2; exit 1; fi
  parsed_bool="$user_input"
  xmlstarlet sel -t -v "//user[name='$parsed_bool']/email" /var/data/users.xml
}

benchmark_test_00024 "$@"
