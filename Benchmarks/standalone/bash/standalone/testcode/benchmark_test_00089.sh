#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00089() {
  user_input="$(tr '&' '\n' | grep '^field=' | cut -d= -f2-)"
  printf '%s' "$user_input" | xmllint --stream --nonet -
}

benchmark_test_00089 "$@"
