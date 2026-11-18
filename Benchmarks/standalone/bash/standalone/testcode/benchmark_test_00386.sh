#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00386() {
  user_input="$(jq -r '.value // empty' 2>/dev/null)"
  data=$(echo "$user_input" | jq -r '.value // empty' 2>/dev/null || echo "")
  echo "$data" | xmllint --noent --nonet - > /dev/null 2>&1
}

benchmark_test_00386 "$@"
