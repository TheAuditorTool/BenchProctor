#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00188() {
  user_input="$USER_COMMENT"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  printf '%s' "$data" | xmllint --stream --noent --nonet -
}

benchmark_test_00188 "$@"
