#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00206() {
  user_input="$HTTP_X_CUSTOM_HEADER"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  xmllint --xpath "//user[name='$processed']" /var/data/users.xml
}

benchmark_test_00206 "$@"
