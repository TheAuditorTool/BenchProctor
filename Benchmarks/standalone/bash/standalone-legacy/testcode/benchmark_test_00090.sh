#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00090() {
  user_input="$APP_INPUT"
  _prefix="${user_input:0:1}"
  case "$_prefix" in
    h|H) data=`printf '%s' "${user_input}" | tr '[:upper:]' '[:lower:]'`;;
    f|F) data=`printf '%s' "${user_input}" | tr '[:lower:]' '[:upper:]'`;;
    *) data="${user_input}";;
  esac
  ldapcompare -x "uid=$data,ou=people,dc=example,dc=com" "accountStatus:active"
}

benchmark_test_00090 "$@"
