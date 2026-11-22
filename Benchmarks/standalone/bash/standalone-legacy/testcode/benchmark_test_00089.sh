#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00089() {
  user_input="`mysql -N -e 'SELECT name FROM users LIMIT 1'`"
  data="${user_input:-default}"
  echo "$data" | xmllint --noent --nonet - > /dev/null 2>&1
}

benchmark_test_00089 "$@"
