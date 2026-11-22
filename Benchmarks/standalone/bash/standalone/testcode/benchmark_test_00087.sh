#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00087() {
  user_input="$(tr '&' '\n' | grep '^field=' | cut -d= -f2-)"
  data=$(printf "%b" "${user_input//%/\\x}")
  _schema_re='^[A-Za-z0-9_][A-Za-z0-9_ @-]*$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  ldapcompare -x "uid=$processed,ou=people,dc=example,dc=com" "accountStatus:active"
}

benchmark_test_00087 "$@"
