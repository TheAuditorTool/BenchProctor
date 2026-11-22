#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00029() {
  user_input="$HTTP_COOKIE"
  _prefix="${user_input:0:1}"
  case "$_prefix" in
    h|H) data=$(printf '%s' "${user_input}" | tr '[:upper:]' '[:lower:]');;
    f|F) data=$(printf '%s' "${user_input}" | tr '[:lower:]' '[:upper:]');;
    *) data="${user_input}";;
  esac
  case $data in config.json|index.html|readme.md) checked_path="/var/app/data/$data";; *) echo "forbidden"; exit 1;; esac
  echo "data" > "$checked_path"
}

benchmark_test_00029 "$@"
