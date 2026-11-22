#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00146() {
  user_input="$HTTP_AUTHORIZATION"
  data=$(echo "$user_input" | xxd -r -p 2>/dev/null || echo "")
  wget -q -O - -T 10 --max-redirect=0 -- "$data"
}

benchmark_test_00146 "$@"
