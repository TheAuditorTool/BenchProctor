#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00187() {
  user_input="$PATH_INFO"
  printf -v data "%s" "${user_input}"
  ldapwhoami -x -D "uid=$data,ou=people,dc=example,dc=com" -y /run/secrets/ldap_bind_password
}

benchmark_test_00187 "$@"
