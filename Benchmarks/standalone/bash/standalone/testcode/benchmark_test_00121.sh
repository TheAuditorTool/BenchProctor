#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00121() {
  user_input="$HTTP_ORIGIN"
  data="${user_input//$'\x00'/}"
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  ldapwhoami -x -D "uid=$processed,ou=people,dc=example,dc=com" -y /run/secrets/ldap_bind_password
}

benchmark_test_00121 "$@"
