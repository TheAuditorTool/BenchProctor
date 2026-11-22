#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00036() {
  user_input="$(cat /dev/stdin)"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  _schema_re='^[a-zA-Z0-9 #%._-]+$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  ldapwhoami -x -D "uid=$processed,ou=people,dc=example,dc=com" -y /run/secrets/ldap_bind_password
}

benchmark_test_00036 "$@"
