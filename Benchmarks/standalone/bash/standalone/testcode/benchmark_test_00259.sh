#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00259() {
  user_input="$(sed -n '/^\r*$/{n;s/\r$//;p;q}')"
  data="${user_input:-default}"
  echo "$data" | xmllint --noent --nonet - > /dev/null 2>&1
}

benchmark_test_00259 "$@"
