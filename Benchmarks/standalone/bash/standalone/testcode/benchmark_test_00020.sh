#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00020() {
  user_input="$HTTP_AUTHORIZATION"
  if _parsed=$(printf "%d" "${user_input}" 2>/dev/null); then
    data="$_parsed"
  else
    data="${user_input}"
  fi
  coerced_float=$(printf "%.6f" "$data" 2>/dev/null) || { echo "invalid float" >&2; exit 1; }
  xmllint --xpath "//user[name='$coerced_float']" /var/data/users.xml
}

benchmark_test_00020 "$@"
