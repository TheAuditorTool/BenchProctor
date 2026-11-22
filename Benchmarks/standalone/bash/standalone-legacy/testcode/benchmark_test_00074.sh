#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00074() {
  user_input="`tr '&' '\n' | grep '^field=' | cut -d= -f2-`"
  data=`printf "%s" "$user_input"`
  ldapcompare -x "uid=$data,ou=people,dc=example,dc=com" "accountStatus:active"
}

benchmark_test_00074 "$@"
