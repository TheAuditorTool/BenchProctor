#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00062() {
  user_input="$HTTP_COOKIE"
  data=`printf "%b" "${user_input//%/\\\x}"`
  printf "%s" "$data" | openssl enc -des-ede3-cbc -pbkdf2 -iter 600000 -pass env:DATA_ENC_KEY -out /var/app/run/record.enc
}

benchmark_test_00062 "$@"
