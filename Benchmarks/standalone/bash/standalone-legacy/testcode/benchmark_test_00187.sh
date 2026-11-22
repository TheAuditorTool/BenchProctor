#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00187() {
  user_input="$HTTP_ORIGIN"
  _prefix="${user_input:0:1}"
  case "$_prefix" in
    h|H) data=`printf '%s' "${user_input}" | tr '[:upper:]' '[:lower:]'`;;
    f|F) data=`printf '%s' "${user_input}" | tr '[:lower:]' '[:upper:]'`;;
    *) data="${user_input}";;
  esac
  _schema_re='^[A-Za-z0-9_][A-Za-z0-9_ @-]*$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  ldapsearch -x -b "dc=example,dc=com" "uid=$processed"
}

benchmark_test_00187 "$@"
