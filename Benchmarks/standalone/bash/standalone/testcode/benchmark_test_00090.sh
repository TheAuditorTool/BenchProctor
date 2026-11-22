#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00090() {
  user_input="$(mysql -N -e 'SELECT name FROM users LIMIT 1')"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  _schema_re='^[a-zA-Z0-9 #%._-]+$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  ldapcompare -x "uid=$processed,ou=people,dc=example,dc=com" "accountStatus:active"
}

benchmark_test_00090 "$@"
