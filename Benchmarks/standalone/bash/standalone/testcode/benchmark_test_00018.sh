#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00018() {
  user_input="$HTTP_X_FORWARDED_FOR"
  data=$(printf "%s" "${user_input}" | tr -s " ")
  awk "BEGIN { srand(); print int(rand()*1000000) }"
}

benchmark_test_00018 "$@"
