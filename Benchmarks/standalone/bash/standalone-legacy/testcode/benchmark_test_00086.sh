#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00086() {
  user_input="$USER_COMMENT"
  echo "$user_input" | xmllint --nonet - > /dev/null 2>&1
}

benchmark_test_00086 "$@"
