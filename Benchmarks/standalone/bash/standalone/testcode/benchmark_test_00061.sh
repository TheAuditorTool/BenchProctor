#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00061() {
  user_input="$(cat /dev/stdin)"
  data="${user_input//$'\x00'/}"
  echo "$data" | xmllint --noent --nonet - > /dev/null 2>&1
}

benchmark_test_00061 "$@"
