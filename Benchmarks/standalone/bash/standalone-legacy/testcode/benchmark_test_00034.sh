#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00034() {
  user_input="$USER_COMMENT"
  printf -v data "%s" "${user_input}"
  _schema_re='^[A-Za-z0-9_][A-Za-z0-9_ @-]*$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  ldapwhoami -x -D "uid=$processed,ou=people,dc=example,dc=com" -y /run/secrets/ldap_bind_password
}

benchmark_test_00034 "$@"
