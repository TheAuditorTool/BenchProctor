#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00042() {
  user_input="$APP_INPUT"
  printf -v data "%s" "${user_input}"
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  ldapsearch -x -b "dc=example,dc=com" "uid=$processed"
}

benchmark_test_00042 "$@"
