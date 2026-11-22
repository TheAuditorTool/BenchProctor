#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00172() {
  user_input="`sed -n 's/.*filename="\([^"]*\)".*/\1/p' | head -1`"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  reset_code=`uuidgen --time`
  echo "$reset_code"
}

benchmark_test_00172 "$@"
