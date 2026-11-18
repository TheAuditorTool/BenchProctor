#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00352() {
  user_input="$USER_COMMENT"
  _prefix="${user_input:0:1}"
  case "$_prefix" in
    h|H) data=$(printf '%s' "${user_input}" | tr '[:upper:]' '[:lower:]');;
    f|F) data=$(printf '%s' "${user_input}" | tr '[:lower:]' '[:upper:]');;
    *) data="${user_input}";;
  esac
  checked_path=$(realpath -m "/var/app/data/$data")
  if [[ ! "$checked_path" == /var/app/data/* ]]; then echo "forbidden" >&2; exit 1; fi
  echo "data" > "$checked_path"
}

benchmark_test_00352 "$@"
