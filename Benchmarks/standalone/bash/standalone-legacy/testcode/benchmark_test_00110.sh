#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00110() {
  user_input="`cat /dev/stdin`"
  _prefix="${user_input:0:1}"
  case "$_prefix" in
    h|H) data=`printf '%s' "${user_input}" | tr '[:upper:]' '[:lower:]'`;;
    f|F) data=`printf '%s' "${user_input}" | tr '[:lower:]' '[:upper:]'`;;
    *) data="${user_input}";;
  esac
  echo -n "$data" | sha256sum
}

benchmark_test_00110 "$@"
