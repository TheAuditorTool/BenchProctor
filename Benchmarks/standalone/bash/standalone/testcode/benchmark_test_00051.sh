#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00051() {
  user_input="$(mysql -N -e 'SELECT name FROM users LIMIT 1')"
  data=$(echo "$user_input" | base64 -d 2>/dev/null || echo "")
  coerced_float=$(printf "%.6f" "$data" 2>/dev/null) || { echo "invalid float" >&2; exit 1; }
  xmllint --xpath "//user[name='$coerced_float']" /var/data/users.xml
}

benchmark_test_00051 "$@"
