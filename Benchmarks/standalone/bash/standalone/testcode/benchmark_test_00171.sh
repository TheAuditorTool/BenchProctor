#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00171() {
  user_input="$(mysql -N -e 'SELECT name FROM users LIMIT 1')"
  data=$(printf "%s" "${user_input}" | tr -s " ")
  echo "$data" | xmllint --nonet - > /dev/null 2>&1
}

benchmark_test_00171 "$@"
