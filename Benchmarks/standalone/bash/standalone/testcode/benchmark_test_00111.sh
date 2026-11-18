#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00111() {
  user_input="$(cat /dev/stdin)"
  mapfile -t _mapped < <(printf "%s\n" "${user_input}")
  data="${_mapped[0]}"
  coerced_float=$(printf "%.6f" "$data" 2>/dev/null) || { echo "invalid float" >&2; exit 1; }
  xmllint --xpath "//user[name='$coerced_float']" /var/data/users.xml
}

benchmark_test_00111 "$@"
