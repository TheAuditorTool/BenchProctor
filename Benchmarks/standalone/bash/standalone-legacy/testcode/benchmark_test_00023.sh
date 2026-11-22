#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00023() {
  user_input="`tr '&' '\n' | grep '^field=' | cut -d= -f2-`"
  _first_line() { IFS= read -r _line; printf '%s' "$_line"; }
  data=`printf "%s\n" "${user_input}" | _first_line`
  echo "$data" | xmllint --noent --nonet - > /dev/null 2>&1
}

benchmark_test_00023 "$@"
