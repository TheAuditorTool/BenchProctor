#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00039() {
  user_input="$HTTP_USER_AGENT"
  data=$(printf "%s" "${user_input}" | tr -s " ")
  local -a _cmd=("echo" "$data")
  "${_cmd[@]}"
}

benchmark_test_00039 "$@"
