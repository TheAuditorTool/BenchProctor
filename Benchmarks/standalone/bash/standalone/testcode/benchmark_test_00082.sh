#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00082() {
  user_input="$(sed -n '/^\r*$/{n;s/\r$//;p;q}')"
  _prefix="${user_input:0:1}"
  case "$_prefix" in
    h|H) data=$(printf '%s' "${user_input}" | tr '[:upper:]' '[:lower:]');;
    f|F) data=$(printf '%s' "${user_input}" | tr '[:lower:]' '[:upper:]');;
    *) data="${user_input}";;
  esac
  _rest="${data#*://}"
  exec 3<>"/dev/tcp/${_rest%%[/:]*}/80"
}

benchmark_test_00082 "$@"
