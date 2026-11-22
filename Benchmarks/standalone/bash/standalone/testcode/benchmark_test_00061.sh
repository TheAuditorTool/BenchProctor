#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00061() {
  user_input="$(mysql -N -e 'SELECT name FROM users LIMIT 1')"
  printf -v data "%s" "${user_input}"
  reset_code="$RANDOM$RANDOM"
  echo "$reset_code"
}

benchmark_test_00061 "$@"
