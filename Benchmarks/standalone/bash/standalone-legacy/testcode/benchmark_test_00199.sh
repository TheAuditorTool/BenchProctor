#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00199() {
  user_input="$PATH_INFO"
  _first_line() { IFS= read -r _line; printf '%s' "$_line"; }
  data=`printf "%s\n" "${user_input}" | _first_line`
  eval echo "~$data"
}

benchmark_test_00199 "$@"
