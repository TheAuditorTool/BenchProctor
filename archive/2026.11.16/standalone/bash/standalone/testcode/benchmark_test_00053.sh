#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00053() {
  user_input="$(sed -n 's/.*filename="\([^"]*\)".*/\1/p' | head -1)"
  data="${user_input//$'\x00'/}"
  awk "BEGIN { srand(); print int(rand()*1000000) }"
}

benchmark_test_00053 "$@"
