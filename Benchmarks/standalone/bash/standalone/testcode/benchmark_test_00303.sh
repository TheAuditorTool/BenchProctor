#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00303() {
  user_input="$QUERY_STRING"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=$(normalize "$user_input")
  awk "BEGIN { srand(); print int(rand()*1000000) }"
}

benchmark_test_00303 "$@"
