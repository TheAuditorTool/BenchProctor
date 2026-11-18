#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00362() {
  user_input="$USER_COMMENT"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  ldapsearch -x -b "dc=example,dc=com" "uid=$data"
}

benchmark_test_00362 "$@"
