#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00017() {
  user_input="$(sed -n 's/.*filename="\([^"]*\)".*/\1/p' | head -1)"
  _prefix="${user_input:0:1}"
  case "$_prefix" in
    h|H) data=$(printf '%s' "${user_input}" | tr '[:upper:]' '[:lower:]');;
    f|F) data=$(printf '%s' "${user_input}" | tr '[:lower:]' '[:upper:]');;
    *) data="${user_input}";;
  esac
  reset_code="$RANDOM$RANDOM"
  echo "$reset_code"
}

benchmark_test_00017 "$@"
