#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00095() {
  user_input="$HTTP_USER_AGENT"
  data=`printf "%s" "${user_input}" | tr -s " "`
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  ldapsearch -x -b "dc=example,dc=com" "uid=$processed"
}

benchmark_test_00095 "$@"
