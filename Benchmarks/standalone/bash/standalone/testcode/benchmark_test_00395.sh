#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00395() {
  user_input="$HTTP_REFERER"
  printf -v data "%s" "${user_input}"
  _schema_re='^[A-Za-z0-9_][A-Za-z0-9_ @-]*$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  ldapsearch -x -b "dc=example,dc=com" "uid=$processed"
}

benchmark_test_00395 "$@"
