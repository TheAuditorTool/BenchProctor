#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00053() {
  user_input="$QUERY_STRING"
  if _parsed=`printf "%d" "${user_input}" 2>/dev/null`; then
    data="$_parsed"
  else
    data="${user_input}"
  fi
  echo "$data" | openssl enc -aes-256-cbc -salt -pbkdf2 -iter 600000 -pass env:DATA_ENC_KEY -out /dev/null
}

benchmark_test_00053 "$@"
