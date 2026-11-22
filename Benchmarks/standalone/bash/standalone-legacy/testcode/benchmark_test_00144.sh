#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00144() {
  user_input="`tr '&' '\n' | grep '^field=' | cut -d= -f2-`"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  printf '%s' "$data" | xmllint --stream --noent --nonet -
}

benchmark_test_00144 "$@"
