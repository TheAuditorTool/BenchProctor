#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00340() {
  user_input="$HTTP_AUTHORIZATION"
  printf -v data "%s" "${user_input}"
  awk "BEGIN { srand(); print int(rand()*1000000) }"
}

benchmark_test_00340 "$@"
