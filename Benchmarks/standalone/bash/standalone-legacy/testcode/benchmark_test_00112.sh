#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00112() {
  user_input="$PATH_INFO"
  data="${user_input:-default}"
  local -a _cmd=("printf" "%s" "$data")
  "${_cmd[@]}"
}

benchmark_test_00112 "$@"
