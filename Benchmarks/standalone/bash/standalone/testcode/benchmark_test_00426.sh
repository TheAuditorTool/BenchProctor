#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00426() {
  user_input="$(jq -r '.value // empty' 2>/dev/null)"
  data=$(echo "$user_input" | jq -r '.value // empty' 2>/dev/null || echo "")
  echo -n "$data" | sha256sum
}

benchmark_test_00426 "$@"
