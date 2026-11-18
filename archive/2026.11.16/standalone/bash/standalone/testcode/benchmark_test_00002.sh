#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00002() {
  user_input="$HTTP_USER_AGENT"
  data="${user_input//$'\x00'/}"
  _schema_re='^[A-Za-z0-9_][A-Za-z0-9_ @-]*$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  xmllint --xpath "//user[name='$processed']" /var/data/users.xml
}

benchmark_test_00002 "$@"
