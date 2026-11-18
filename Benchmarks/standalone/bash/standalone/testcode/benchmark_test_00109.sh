#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00109() {
  user_input="$HTTP_X_CUSTOM_HEADER"
  data=$(printf "%s" "$user_input")
  local -a _cmd=("echo" "$data")
  "${_cmd[@]}"
}

benchmark_test_00109 "$@"
