#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00148() {
  user_input="`mysql -N -e 'SELECT name FROM users LIMIT 1'`"
  printf -v data "%s" "${user_input}"
  _schema_re='^[A-Za-z0-9_][A-Za-z0-9_ @-]*$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  xsltproc --param user "'$processed'" /etc/app/user_lookup.xsl /var/data/users.xml
}

benchmark_test_00148 "$@"
