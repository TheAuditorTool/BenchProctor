#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00059() {
  user_input="$HTTP_REFERER"
  data=`printf "%s" "${user_input}" | tr -s " "`
  _schema_re='^[A-Za-z0-9_][A-Za-z0-9_ @-]*$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  xmlstarlet sel -t -v "//user[name='$processed']/email" /var/data/users.xml
}

benchmark_test_00059 "$@"
