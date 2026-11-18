#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00029() {
  user_input="$(cat /dev/stdin)"
  data=$(printf "%s" "${user_input}" | tr -s " ")
  echo "$data" | xmllint --noent --nonet - > /dev/null 2>&1
}

benchmark_test_00029 "$@"
