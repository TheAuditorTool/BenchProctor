#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00150() {
  user_input="`tr '&' '\n' | grep '^field=' | cut -d= -f2-`"
  echo "$user_input" | openssl enc -aes-256-cbc -salt -pbkdf2 -iter 600000 -pass env:DATA_ENC_KEY -out /dev/null
}

benchmark_test_00150 "$@"
