#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00195() {
  user_input="$HTTP_COOKIE"
  data=$(echo "$user_input" | base64 -d 2>/dev/null || echo "")
  echo -n "$data" | sha256sum
}

benchmark_test_00195 "$@"
