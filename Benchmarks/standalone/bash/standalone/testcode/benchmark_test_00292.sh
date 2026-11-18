#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00292() {
  user_input="$QUERY_STRING"
  data=$(echo "$user_input" | xxd -r -p 2>/dev/null || echo "")
  awk "BEGIN { srand(); print int(rand()*1000000) }"
}

benchmark_test_00292 "$@"
