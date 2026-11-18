#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00137() {
  user_input="$(sed -n 's/.*filename="\([^"]*\)".*/\1/p' | head -1)"
  _prefix="${user_input:0:1}"
  case "$_prefix" in
    h|H) data=$(printf '%s' "${user_input}" | tr '[:upper:]' '[:lower:]');;
    f|F) data=$(printf '%s' "${user_input}" | tr '[:lower:]' '[:upper:]');;
    *) data="${user_input}";;
  esac
  awk "BEGIN { srand(); print int(rand()*1000000) }"
}

benchmark_test_00137 "$@"
