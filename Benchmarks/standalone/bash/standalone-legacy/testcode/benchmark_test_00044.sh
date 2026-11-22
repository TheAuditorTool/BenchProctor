#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00044() {
  user_input="$PATH_INFO"
  _first_line() { IFS= read -r _line; printf '%s' "$_line"; }
  data=`printf "%s\n" "${user_input}" | _first_line`
  printf '%s' "$data" | openssl enc -aes-256-ctr -pbkdf2 -iter 600000 -pass env:DATA_ENC_KEY -out /var/app/run/record.enc
}

benchmark_test_00044 "$@"
