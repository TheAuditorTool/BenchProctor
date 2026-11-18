#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00059() {
  user_input="$APP_INPUT"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=$(make_reader)
  awk "BEGIN { srand(); print int(rand()*1000000) }"
}

benchmark_test_00059 "$@"
