#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00149() {
  user_input="$(mysql -N -e 'SELECT name FROM users LIMIT 1')"
  data="${user_input:-default}"
  _schema_re='^[a-zA-Z0-9 #%._-]+$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  ldapsearch -x -b "dc=example,dc=com" "uid=$processed"
}

benchmark_test_00149 "$@"
