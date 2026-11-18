#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00343() {
  user_input="$HTTP_X_CUSTOM_HEADER"
  if _parsed=$(printf "%d" "${user_input}" 2>/dev/null); then
    data="$_parsed"
  else
    data="${user_input}"
  fi
  _schema_re='^[A-Za-z0-9_][A-Za-z0-9_ @-]*$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  ldapsearch -x -b "dc=example,dc=com" "uid=$processed"
}

benchmark_test_00343 "$@"
