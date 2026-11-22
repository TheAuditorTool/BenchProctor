#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00074() {
  user_input="$(sed -n 's/.*filename="\([^"]*\)".*/\1/p' | head -1)"
  _prefix="${user_input:0:1}"
  case "$_prefix" in
    h|H) data=$(printf '%s' "${user_input}" | tr '[:upper:]' '[:lower:]');;
    f|F) data=$(printf '%s' "${user_input}" | tr '[:lower:]' '[:upper:]');;
    *) data="${user_input}";;
  esac
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  ldapwhoami -x -D "uid=$processed,ou=people,dc=example,dc=com" -y /run/secrets/ldap_bind_password
}

benchmark_test_00074 "$@"
