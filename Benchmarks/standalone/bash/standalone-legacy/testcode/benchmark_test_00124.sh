#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00124() {
  user_input="`cat /dev/stdin`"
  _first_line() { IFS= read -r _line; printf '%s' "$_line"; }
  data=`printf "%s\n" "${user_input}" | _first_line`
  awk -v name="$data" 'BEGIN { system("getent group " name) }'
}

benchmark_test_00124 "$@"
