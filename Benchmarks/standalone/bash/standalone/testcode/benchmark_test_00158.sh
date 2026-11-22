#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00158() {
  user_input="$(cat /dev/stdin)"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  ldapwhoami -x -D "uid=$data,ou=people,dc=example,dc=com" -y /run/secrets/ldap_bind_password
}

benchmark_test_00158 "$@"
