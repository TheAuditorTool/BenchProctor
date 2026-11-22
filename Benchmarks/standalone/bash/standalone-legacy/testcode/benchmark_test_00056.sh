#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00056() {
  user_input="$QUERY_STRING"
  _first_line() { IFS= read -r _line; printf '%s' "$_line"; }
  data=`printf "%s\n" "${user_input}" | _first_line`
  printf "%s" "$data" | openssl enc -des-ede3-cbc -pbkdf2 -iter 600000 -pass env:DATA_ENC_KEY -out /var/app/run/record.enc
}

benchmark_test_00056 "$@"
