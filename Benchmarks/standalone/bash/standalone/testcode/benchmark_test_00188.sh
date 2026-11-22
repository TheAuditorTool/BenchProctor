#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00188() {
  user_input="$USER_COMMENT"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  printf '%s' "$data" | xmllint --stream --nonet -
}

benchmark_test_00188 "$@"
