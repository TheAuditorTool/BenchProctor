#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00409() {
  user_input="$(cat /dev/stdin)"
  data=$(printf "%s" "$user_input")
  echo "$data" | xmllint --noent --nonet - > /dev/null 2>&1
}

benchmark_test_00409 "$@"
