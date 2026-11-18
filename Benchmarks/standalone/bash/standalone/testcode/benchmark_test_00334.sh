#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00334() {
  user_input="$(sed -n '/^\r*$/{n;s/\r$//;p;q}')"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=$(make_reader)
  echo "$data" | xmllint --noent --nonet - > /dev/null 2>&1
}

benchmark_test_00334 "$@"
