#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00243() {
  user_input="$(sed -n 's/.*filename="\([^"]*\)".*/\1/p' | head -1)"
  printf -v data "%s" "${user_input}"
  coerced_float=$(printf "%.6f" "$data" 2>/dev/null) || { echo "invalid float" >&2; exit 1; }
  xmllint --xpath "//user[name='$coerced_float']" /var/data/users.xml
}

benchmark_test_00243 "$@"
