#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00072() {
  user_input="$(tr '&' '\n' | grep '^field=' | cut -d= -f2-)"
  data=$(printf "%s" "${user_input}" | tr -s " ")
  echo "$data" | xmllint --nonet - > /dev/null 2>&1
}

benchmark_test_00072 "$@"
