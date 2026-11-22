#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00190() {
  user_input="`tr '&' '\n' | grep '^field=' | cut -d= -f2-`"
  _first_line() { IFS= read -r _line; printf '%s' "$_line"; }
  data=`printf "%s\n" "${user_input}" | _first_line`
  _schema_re='^[a-zA-Z0-9#._-]+$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  mysql -e "SELECT * FROM users WHERE id = '$processed'"
}

benchmark_test_00190 "$@"
