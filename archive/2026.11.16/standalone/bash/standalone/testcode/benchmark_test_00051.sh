#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00051() {
  user_input="$(sed -n '/^\r*$/{n;s/\r$//;p;q}')"
  printf -v data "%s" "${user_input}"
  echo "$data" | xmllint --nonet - > /dev/null 2>&1
}

benchmark_test_00051 "$@"
