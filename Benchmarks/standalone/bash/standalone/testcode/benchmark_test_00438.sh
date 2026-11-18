#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00438() {
  user_input="$HTTP_USER_AGENT"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=$(normalize "$user_input")
  local -a _cmd=("printf" "%s" "$data")
  "${_cmd[@]}"
}

benchmark_test_00438 "$@"
