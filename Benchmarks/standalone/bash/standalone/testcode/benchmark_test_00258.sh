#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00258() {
  user_input="$HTTP_REFERER"
  data=$(printf "%b" "${user_input//%/\\x}")
  awk "BEGIN { srand(); print int(rand()*1000000) }"
}

benchmark_test_00258 "$@"
