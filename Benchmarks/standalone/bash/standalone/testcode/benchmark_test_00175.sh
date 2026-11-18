#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00175() {
  user_input="$(tr '&' '\n' | grep '^field=' | cut -d= -f2-)"
  awk "BEGIN { srand(); print int(rand()*1000000) }"
}

benchmark_test_00175 "$@"
