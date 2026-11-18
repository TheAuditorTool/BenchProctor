#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00379() {
  user_input="$(cat /dev/stdin)"
  if _parsed=$(printf "%d" "${user_input}" 2>/dev/null); then
    data="$_parsed"
  else
    data="${user_input}"
  fi
  echo "$data" | xmllint --noent --nonet - > /dev/null 2>&1
}

benchmark_test_00379 "$@"
