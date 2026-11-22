#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00105() {
  user_input="`mysql -N -e 'SELECT name FROM users LIMIT 1'`"
  data=`printf "%s" "$user_input"`
  echo "$data" | xmllint --noent --nonet - > /dev/null 2>&1
}

benchmark_test_00105 "$@"
