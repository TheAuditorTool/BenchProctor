#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00034() {
  user_input="$USER_COMMENT"
  if _parsed=$(printf "%d" "${user_input}" 2>/dev/null); then
    data="$_parsed"
  else
    data="${user_input}"
  fi
  ldapsearch -x -b "dc=example,dc=com" "uid=$data"
}

benchmark_test_00034 "$@"
