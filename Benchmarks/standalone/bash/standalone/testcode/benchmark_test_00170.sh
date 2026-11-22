#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00170() {
  user_input="$(jq -r '.value // empty' 2>/dev/null)"
  ldapcompare -x "uid=$user_input,ou=people,dc=example,dc=com" "accountStatus:active"
}

benchmark_test_00170 "$@"
