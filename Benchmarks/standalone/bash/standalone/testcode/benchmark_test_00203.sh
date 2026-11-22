#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00203() {
  user_input="$(sed -n '/^\r*$/{n;s/\r$//;p;q}')"
  ldapsearch -x -b "dc=example,dc=com" "uid=$user_input"
}

benchmark_test_00203 "$@"
