#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00239() {
  user_input="$(cat /dev/stdin)"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  eval "echo $data"
}

benchmark_test_00239 "$@"
