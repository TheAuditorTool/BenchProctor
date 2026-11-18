#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00003() {
  user_input="$1"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  local -a _cmd=("printf" "%s" "$data")
  "${_cmd[@]}"
}

benchmark_test_00003 "$@"
