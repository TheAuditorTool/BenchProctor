#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00114() {
  user_input="$(tr '&' '\n' | grep '^field=' | cut -d= -f2-)"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=$(make_reader)
  echo "$data" | xmllint --nonet - > /dev/null 2>&1
}

benchmark_test_00114 "$@"
