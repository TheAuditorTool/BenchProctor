#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00135() {
  user_input="`cat /dev/stdin`"
  printf -v data "%s" "${user_input}"
  printf '%s' "$data" | xmllint --stream --noent --nonet -
}

benchmark_test_00135 "$@"
