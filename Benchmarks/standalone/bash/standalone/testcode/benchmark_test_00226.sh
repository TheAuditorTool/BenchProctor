#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00226() {
  user_input="$USER_COMMENT"
  data=$(printf "%s" "$user_input")
  awk "BEGIN { srand(); print int(rand()*1000000) }"
}

benchmark_test_00226 "$@"
