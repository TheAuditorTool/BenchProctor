#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00238() {
  user_input="$HTTP_ORIGIN"
  if _parsed=$(printf "%d" "${user_input}" 2>/dev/null); then
    data="$_parsed"
  else
    data="${user_input}"
  fi
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  ldapsearch -x -b "dc=example,dc=com" "uid=$processed"
}

benchmark_test_00238 "$@"
