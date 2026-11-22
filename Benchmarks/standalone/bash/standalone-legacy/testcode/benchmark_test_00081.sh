#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00081() {
  user_input="`jq -r '.value // empty' 2>/dev/null`"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=`make_reader`
  local -a _cmd=("printf" "%s" "$data")
  "${_cmd[@]}"
}

benchmark_test_00081 "$@"
