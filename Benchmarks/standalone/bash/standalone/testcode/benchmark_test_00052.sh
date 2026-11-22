#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00052() {
  user_input="$(cat /dev/stdin)"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=$(make_reader)
  awk "BEGIN { srand(); print int(rand()*1000000) }"
}

benchmark_test_00052 "$@"
