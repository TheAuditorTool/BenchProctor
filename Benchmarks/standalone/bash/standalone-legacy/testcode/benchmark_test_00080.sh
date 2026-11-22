#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00080() {
  user_input="$HTTP_USER_AGENT"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=`normalize "$user_input"`
  ldapwhoami -x -D "uid=$data,ou=people,dc=example,dc=com" -y /run/secrets/ldap_bind_password
}

benchmark_test_00080 "$@"
