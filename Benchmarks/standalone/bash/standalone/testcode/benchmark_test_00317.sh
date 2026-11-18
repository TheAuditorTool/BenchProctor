#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00317() {
  user_input="$PATH_INFO"
  data="${user_input:-default}"
  _int_re='^-?[0-9]+$'
  if [[ ! "$data" =~ $_int_re ]]; then echo "invalid"; exit 1; fi
  parsed_id="$data"
  mysql -e "SELECT * FROM users WHERE id = $parsed_id"
}

benchmark_test_00317 "$@"
