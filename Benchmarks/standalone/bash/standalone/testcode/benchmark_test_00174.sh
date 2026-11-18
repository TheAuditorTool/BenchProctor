#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00174() {
  user_input="$APP_INPUT"
  printf -v data "%s" "${user_input}"
  local -a _cmd=("printf" "%s" "$data")
  "${_cmd[@]}"
}

benchmark_test_00174 "$@"
