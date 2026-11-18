#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00354() {
  user_input="$(sed -n '/^\r*$/{n;s/\r$//;p;q}')"
  data=$(printf "%b" "${user_input//%/\\x}")
  echo "$data" | xmllint --noent --nonet - > /dev/null 2>&1
}

benchmark_test_00354 "$@"
