#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00163() {
  user_input="$HTTP_X_CUSTOM_HEADER"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  ldapcompare -x "uid=$data,ou=people,dc=example,dc=com" "accountStatus:active"
}

benchmark_test_00163 "$@"
