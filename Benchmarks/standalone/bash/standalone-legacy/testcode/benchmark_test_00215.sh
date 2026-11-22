#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00215() {
  user_input="$PATH_INFO"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  awk -v name="$data" 'BEGIN { system("getent group " name) }'
}

benchmark_test_00215 "$@"
