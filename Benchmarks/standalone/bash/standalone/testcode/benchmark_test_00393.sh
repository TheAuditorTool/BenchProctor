#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00393() {
  user_input="$(cat /etc/app/config)"
  printf -v data "%s" "${user_input}"
  _int_re='^-?[0-9]+$'
  if [[ ! "$data" =~ $_int_re ]]; then echo "invalid"; exit 1; fi
  parsed_id="$data"
  mysql -e "SELECT * FROM users WHERE id = $parsed_id"
}

benchmark_test_00393 "$@"
