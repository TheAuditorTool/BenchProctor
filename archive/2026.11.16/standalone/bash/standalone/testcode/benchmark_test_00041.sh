#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00041() {
  user_input="$HTTP_COOKIE"
  data="${user_input:-default}"
  local -a _cmd=("echo" "$data")
  "${_cmd[@]}"
}

benchmark_test_00041 "$@"
