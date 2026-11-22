#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00143() {
  user_input="$HTTP_X_FORWARDED_FOR"
  if _parsed=`printf "%d" "${user_input}" 2>/dev/null`; then
    data="$_parsed"
  else
    data="${user_input}"
  fi
  awk "BEGIN { srand(); print int(rand()*1000000) }"
}

benchmark_test_00143 "$@"
