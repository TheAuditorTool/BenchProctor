#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00219() {
  user_input="$(mysql -N -e 'SELECT name FROM users LIMIT 1')"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  reset_code=$(uuidgen --time)
  echo "$reset_code"
}

benchmark_test_00219 "$@"
