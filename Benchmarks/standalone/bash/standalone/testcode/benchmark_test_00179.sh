#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00179() {
  user_input="$(cat /dev/stdin)"
  data=$(echo "$user_input" | base64 -d 2>/dev/null || echo "")
  echo -n "$data" | md5sum
}

benchmark_test_00179 "$@"
