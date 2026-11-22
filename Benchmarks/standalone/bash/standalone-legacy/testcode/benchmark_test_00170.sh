#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00170() {
  user_input="$HTTP_HOST"
  if _parsed=`printf "%d" "${user_input}" 2>/dev/null`; then
    data="$_parsed"
  else
    data="${user_input}"
  fi
  ldapcompare -x "uid=$data,ou=people,dc=example,dc=com" "accountStatus:active"
}

benchmark_test_00170 "$@"
