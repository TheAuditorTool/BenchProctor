#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00133() {
  user_input="`mysql -N -e 'SELECT name FROM users LIMIT 1'`"
  data=`echo "$user_input" | xxd -r -p 2>/dev/null || echo ""`
  printf '%s' "$data" | xmllint --stream --nonet -
}

benchmark_test_00133 "$@"
