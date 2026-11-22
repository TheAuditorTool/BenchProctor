#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00086() {
  user_input="$USER_COMMENT"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=$(make_reader)
  printf '%s' "$data" | xmllint --stream --nonet -
}

benchmark_test_00086 "$@"
