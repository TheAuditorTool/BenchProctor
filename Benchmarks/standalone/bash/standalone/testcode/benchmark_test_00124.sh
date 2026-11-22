#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00124() {
  user_input="$(cat /dev/stdin)"
  printf -v data "%s" "${user_input}"
  eval echo "~$data"
}

benchmark_test_00124 "$@"
