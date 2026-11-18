#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00253() {
  user_input="$APP_INPUT"
  data=$(printf "%s" "$user_input")
  ldapsearch -x -b "dc=example,dc=com" "uid=$data"
}

benchmark_test_00253 "$@"
