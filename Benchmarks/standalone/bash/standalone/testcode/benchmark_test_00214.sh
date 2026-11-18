#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00214() {
  user_input="$(tr '&' '\n' | grep '^field=' | cut -d= -f2-)"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  echo "$data" | xmllint --noent --nonet - > /dev/null 2>&1
}

benchmark_test_00214 "$@"
