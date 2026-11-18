#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00415() {
  user_input="$USER_COMMENT"
  data=$(printf "%s" "$user_input")
  echo "$data" | xmllint --nonet - > /dev/null 2>&1
}

benchmark_test_00415 "$@"
