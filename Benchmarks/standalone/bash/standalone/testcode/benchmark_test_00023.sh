#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00023() {
  user_input="$HTTP_ORIGIN"
  printf -v data "%s" "${user_input}"
  _schema_re='^[a-zA-Z0-9 %._~-]+$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  xmllint --xpath "//user[name='$processed']" /var/data/users.xml
}

benchmark_test_00023 "$@"
