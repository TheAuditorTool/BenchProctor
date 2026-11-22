#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00024() {
  user_input="$HTTP_REFERER"
  _first_line() { IFS= read -r _line; printf '%s' "$_line"; }
  data=`printf "%s\n" "${user_input}" | _first_line`
  xmllint --xpath "//user[name='$data']" /var/data/users.xml
}

benchmark_test_00024 "$@"
