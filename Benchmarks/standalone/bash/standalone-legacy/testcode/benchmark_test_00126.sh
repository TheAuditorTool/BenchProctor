#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00126() {
  user_input="$HTTP_USER_AGENT"
  data="${user_input:-default}"
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  xmllint --xpath "//user[name='$processed']" /var/data/users.xml
}

benchmark_test_00126 "$@"
