#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00223() {
  user_input="$(cat /dev/stdin)"
  printf -v data "%s" "${user_input}"
  ldapsearch -x -b "dc=example,dc=com" "uid=$data"
}

benchmark_test_00223 "$@"
