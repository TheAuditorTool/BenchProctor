#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00094() {
  user_input="$HTTP_X_FORWARDED_FOR"
  printf -v data "%s" "${user_input}"
  printf "%s" "$data" | openssl enc -des-ede3-cbc -pbkdf2 -iter 600000 -pass env:DATA_ENC_KEY -out /var/app/run/record.enc
}

benchmark_test_00094 "$@"
