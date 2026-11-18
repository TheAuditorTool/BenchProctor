#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00306() {
  user_input="$(jq -r '.value // empty' 2>/dev/null)"
  data="${user_input//$'\x00'/}"
  echo "$data" | xmllint --nonet - > /dev/null 2>&1
}

benchmark_test_00306 "$@"
