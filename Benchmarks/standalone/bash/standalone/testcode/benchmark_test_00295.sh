#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00295() {
  user_input="$(cat /dev/stdin)"
  echo "$user_input" | xmllint --nonet - > /dev/null 2>&1
}

benchmark_test_00295 "$@"
