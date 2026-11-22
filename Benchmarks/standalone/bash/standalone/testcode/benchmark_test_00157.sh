#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00157() {
  user_input="$QUERY_STRING"
  _prefix="${user_input:0:1}"
  case "$_prefix" in
    h|H) data=$(printf '%s' "${user_input}" | tr '[:upper:]' '[:lower:]');;
    f|F) data=$(printf '%s' "${user_input}" | tr '[:lower:]' '[:upper:]');;
    *) data="${user_input}";;
  esac
  printf '%s' "$data" | openssl dgst -md4 -provider legacy -provider default
}

benchmark_test_00157 "$@"
