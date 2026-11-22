#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00160() {
  user_input="$APP_INPUT"
  data="${user_input:-default}"
  echo "$data" | openssl enc -aes-256-cbc -salt -pbkdf2 -iter 600000 -pass env:DATA_ENC_KEY -out /dev/null
}

benchmark_test_00160 "$@"
