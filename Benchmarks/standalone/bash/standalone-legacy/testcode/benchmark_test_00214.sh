#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00214() {
  user_input="`sed -n '/^\r*$/{n;s/\r$//;p;q}'`"
  data=`printf "%s" "${user_input}" | tr -s " "`
  printf '%s' "$data" | openssl enc -aes-256-ecb -pbkdf2 -iter 600000 -pass env:DATA_ENC_KEY -out /var/app/run/record.enc
}

benchmark_test_00214 "$@"
