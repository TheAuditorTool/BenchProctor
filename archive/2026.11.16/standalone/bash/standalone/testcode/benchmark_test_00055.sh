#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00055() {
  user_input="$(mysql -N -e 'SELECT name FROM users LIMIT 1')"
  data=$(echo "$user_input" | base64 -d 2>/dev/null || echo "")
  awk "BEGIN { srand(); print int(rand()*1000000) }"
}

benchmark_test_00055 "$@"
