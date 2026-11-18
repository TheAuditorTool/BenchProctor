#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00145() {
  user_input="$(mysql -N -e 'SELECT name FROM users LIMIT 1')"
  data=$(echo "$user_input" | xxd -r -p 2>/dev/null || echo "")
  echo -n "$data" | md5sum
}

benchmark_test_00145 "$@"
