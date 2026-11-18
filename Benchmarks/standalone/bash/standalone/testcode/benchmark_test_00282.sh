#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00282() {
  user_input="$(tr '&' '\n' | grep '^field=' | cut -d= -f2-)"
  local -a _cmd=("printf" "%s" "$user_input")
  "${_cmd[@]}"
}

benchmark_test_00282 "$@"
