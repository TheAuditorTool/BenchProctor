#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00135() {
  user_input="$(cat /dev/stdin)"
  data="${user_input//$'\x00'/}"
  printf '%s' "$data" | xmllint --stream --noent --nonet -
}

benchmark_test_00135 "$@"
