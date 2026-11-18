#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00423() {
  user_input="$HTTP_X_FORWARDED_FOR"
  printf -v data "%s" "${user_input}"
  awk "BEGIN { srand(); print int(rand()*1000000) }"
}

benchmark_test_00423 "$@"
