#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00163() {
  user_input="$HTTP_HOST"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  ldapwhoami -x -D "uid=$data,ou=people,dc=example,dc=com" -y /run/secrets/ldap_bind_password
}

benchmark_test_00163 "$@"
