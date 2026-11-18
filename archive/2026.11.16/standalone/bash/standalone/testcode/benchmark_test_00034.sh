#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00034() {
  user_input="$(mysql -N -e 'SELECT name FROM users LIMIT 1')"
  data="${user_input:-default}"
  _schema_re='^[a-zA-Z0-9 %._~-]+$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  xmllint --xpath "//user[name='$processed']" /var/data/users.xml
}

benchmark_test_00034 "$@"
