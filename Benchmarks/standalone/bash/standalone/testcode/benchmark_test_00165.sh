#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00165() {
  user_input="$PATH_INFO"
  data=$(printf "%b" "${user_input//%/\\x}")
  awk "BEGIN { srand(); print int(rand()*1000000) }"
}

benchmark_test_00165 "$@"
