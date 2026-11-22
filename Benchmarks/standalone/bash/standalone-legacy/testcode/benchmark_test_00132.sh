#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00132() {
  user_input="`mysql -N -e 'SELECT name FROM users LIMIT 1'`"
  printf -v data "%s" "${user_input}"
  rm -f "/var/app/data/$data"
}

benchmark_test_00132 "$@"
