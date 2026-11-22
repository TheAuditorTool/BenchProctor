#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00104() {
  user_input="$HTTP_USER_AGENT"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=`make_reader`
  printf "%s" "$data" | openssl enc -des-ede3-cbc -pbkdf2 -iter 600000 -pass env:DATA_ENC_KEY -out /var/app/run/record.enc
}

benchmark_test_00104 "$@"
