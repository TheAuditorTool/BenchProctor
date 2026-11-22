#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00178() {
  user_input="$(sed -n '/^\r*$/{n;s/\r$//;p;q}')"
  _prefix="${user_input:0:1}"
  case "$_prefix" in
    h|H) data=$(printf '%s' "${user_input}" | tr '[:upper:]' '[:lower:]');;
    f|F) data=$(printf '%s' "${user_input}" | tr '[:lower:]' '[:upper:]');;
    *) data="${user_input}";;
  esac
  printf "%s" "$data" | openssl enc -des-ede3-cbc -pbkdf2 -iter 600000 -pass env:DATA_ENC_KEY -out /var/app/run/record.enc
}

benchmark_test_00178 "$@"
