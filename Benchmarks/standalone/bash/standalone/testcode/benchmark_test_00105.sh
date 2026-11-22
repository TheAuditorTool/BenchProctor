#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00105() {
  user_input="$(mysql -N -e 'SELECT name FROM users LIMIT 1')"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  printf '%s' "$data" | xmllint --nonet --dropdtd - | xsltproc --nonet /etc/app/order_summary.xsl -
}

benchmark_test_00105 "$@"
