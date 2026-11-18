#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00359() {
  user_input="$(cat /dev/stdin)"
  data=$(printf "%b" "$user_input")
  local -a _cmd=("printf" "%s" "$data")
  "${_cmd[@]}"
}

benchmark_test_00359 "$@"
