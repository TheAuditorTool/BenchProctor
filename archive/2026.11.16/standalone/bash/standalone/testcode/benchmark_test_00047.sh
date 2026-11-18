#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00047() {
  user_input="$(tr '&' '\n' | grep '^field=' | cut -d= -f2-)"
  mapfile -t _mapped < <(printf "%s\n" "${user_input}")
  data="${_mapped[0]}"
  echo "$data" | xmllint --nonet - > /dev/null 2>&1
}

benchmark_test_00047 "$@"
