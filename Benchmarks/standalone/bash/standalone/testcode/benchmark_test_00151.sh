#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00151() {
  user_input="$(jq -r '.value // empty' 2>/dev/null)"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  printf '%s' "$data" | sha512sum
}

benchmark_test_00151 "$@"
