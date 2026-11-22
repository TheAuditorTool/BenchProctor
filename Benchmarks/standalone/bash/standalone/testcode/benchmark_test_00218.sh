#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00218() {
  user_input="$HTTP_COOKIE"
  data="${user_input//$'\x00'/}"
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  ldapcompare -x "uid=$processed,ou=people,dc=example,dc=com" "accountStatus:active"
}

benchmark_test_00218 "$@"
