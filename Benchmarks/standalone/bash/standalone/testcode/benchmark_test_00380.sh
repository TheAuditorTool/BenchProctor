#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00380() {
  user_input="$(cat /dev/stdin)"
  data=$(echo "$user_input" | base64 -d 2>/dev/null || echo "")
  echo "$data" | xmllint --nonet - > /dev/null 2>&1
}

benchmark_test_00380 "$@"
