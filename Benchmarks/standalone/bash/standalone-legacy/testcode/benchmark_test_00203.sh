#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00203() {
  user_input="`jq -r '.value // empty' 2>/dev/null`"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  ldapcompare -x "uid=$processed,ou=people,dc=example,dc=com" "accountStatus:active"
}

benchmark_test_00203 "$@"
