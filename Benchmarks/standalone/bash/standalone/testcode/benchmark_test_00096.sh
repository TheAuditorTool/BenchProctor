#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00096() {
  user_input="$HTTP_X_CUSTOM_HEADER"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=$(make_reader)
  _bool_re='^(true|false|1|0)$'
  if [[ ! "$data" =~ $_bool_re ]]; then echo "invalid bool" >&2; exit 1; fi
  parsed_bool="$data"
  xmllint --xpath "//user[name='$parsed_bool']" /var/data/users.xml
}

benchmark_test_00096 "$@"
