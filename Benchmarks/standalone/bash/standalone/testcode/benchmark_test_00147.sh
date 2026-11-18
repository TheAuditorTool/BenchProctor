#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00147() {
  user_input="$HTTP_X_CUSTOM_HEADER"
  data=$(printf "%s" "$user_input")
  awk "BEGIN { srand(); print int(rand()*1000000) }"
}

benchmark_test_00147 "$@"
