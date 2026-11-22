#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00112() {
  user_input="$QUERY_STRING"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=$(normalize "$user_input")
  local -a _cmd=("echo" "$data")
  "${_cmd[@]}"
}

benchmark_test_00112 "$@"
