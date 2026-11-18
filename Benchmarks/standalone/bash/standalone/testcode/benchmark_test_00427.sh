#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00427() {
  user_input="$(jq -r '.value // empty' 2>/dev/null)"
  _prefix="${user_input:0:1}"
  case "$_prefix" in
    h|H) data=$(printf '%s' "${user_input}" | tr '[:upper:]' '[:lower:]');;
    f|F) data=$(printf '%s' "${user_input}" | tr '[:lower:]' '[:upper:]');;
    *) data="${user_input}";;
  esac
  checked_path="/var/app/data/$(basename -- "$data")"
  echo "data" > "$checked_path"
}

benchmark_test_00427 "$@"
