#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00055() {
  user_input="$QUERY_STRING"
  data="${user_input//$'\x00'/}"
  ldapwhoami -x -D "uid=$data,ou=people,dc=example,dc=com" -y /run/secrets/ldap_bind_password
}

benchmark_test_00055 "$@"
