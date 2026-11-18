#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00398() {
  user_input="$(mysql -N -e 'SELECT name FROM users LIMIT 1')"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  echo "$data" | xmllint --nonet - > /dev/null 2>&1
}

benchmark_test_00398 "$@"
