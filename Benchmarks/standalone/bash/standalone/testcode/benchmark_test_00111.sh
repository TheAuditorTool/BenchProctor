#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00111() {
  user_input="$(sed -n '/^\r*$/{n;s/\r$//;p;q}')"
  data="${user_input//$'\x00'/}"
  echo "$data" | openssl enc -aes-256-cbc -salt -pbkdf2 -iter 600000 -pass env:DATA_ENC_KEY -out /dev/null
}

benchmark_test_00111 "$@"
