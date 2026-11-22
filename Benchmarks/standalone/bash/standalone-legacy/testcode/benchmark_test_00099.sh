#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00099() {
  user_input="$APP_INPUT"
  data=""
  while IFS= read -r line || [ -n "$line" ]; do data+="$line"$'\n'; done <<< "$user_input"
  data="${data%$'\n'}"
  ldapwhoami -x -D "uid=$data,ou=people,dc=example,dc=com" -y /run/secrets/ldap_bind_password
}

benchmark_test_00099 "$@"
