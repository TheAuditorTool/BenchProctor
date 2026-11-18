#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00037() {
  user_input="$(sed -n 's/.*filename="\([^"]*\)".*/\1/p' | head -1)"
  _prefix="${user_input:0:1}"
  case "$_prefix" in
    h|H) data=$(printf '%s' "${user_input}" | tr '[:upper:]' '[:lower:]');;
    f|F) data=$(printf '%s' "${user_input}" | tr '[:lower:]' '[:upper:]');;
    *) data="${user_input}";;
  esac
  printf "%s" "$data" | openssl enc -des-ede3-cbc -K "$DATA_ENC_KEY" -iv "$(openssl rand -hex 8)" -out /var/app/run/record.enc
}

benchmark_test_00037 "$@"
