#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00162() {
  user_input="$(sed -n '/^\r*$/{n;s/\r$//;p;q}')"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  ldapcompare -x "uid=$data,ou=people,dc=example,dc=com" "accountStatus:active"
}

benchmark_test_00162 "$@"
