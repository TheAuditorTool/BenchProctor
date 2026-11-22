#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00079() {
  user_input="$1"
  data="${user_input//$'\x00'/}"
  local -a _cmd=("printf" "%s" "$data")
  "${_cmd[@]}"
}

benchmark_test_00079 "$@"
