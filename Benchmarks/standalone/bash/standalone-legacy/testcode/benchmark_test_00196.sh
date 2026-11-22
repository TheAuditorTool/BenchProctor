#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00196() {
  user_input="`sed -n 's/.*filename="\([^"]*\)".*/\1/p' | head -1`"
  awk "BEGIN { srand(); print int(rand()*1000000) }"
}

benchmark_test_00196 "$@"
