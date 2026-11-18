#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00405() {
  user_input="$(sed -n '/^\r*$/{n;s/\r$//;p;q}')"
  data="${user_input:-default}"
  echo "$data" | xmllint --nonet - > /dev/null 2>&1
}

benchmark_test_00405 "$@"
