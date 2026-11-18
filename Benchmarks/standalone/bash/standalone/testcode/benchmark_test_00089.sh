#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00089() {
  user_input="$PATH_INFO"
  data=$(printf "%s" "${user_input}" | tr -s " ")
  ldapsearch -x -b "dc=example,dc=com" "uid=$data"
}

benchmark_test_00089 "$@"
