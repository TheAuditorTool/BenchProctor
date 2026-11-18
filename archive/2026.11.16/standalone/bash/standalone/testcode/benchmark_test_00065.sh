#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00065() {
  user_input="$(mysql -N -e 'SELECT name FROM users LIMIT 1')"
  _int_re='^-?[0-9]+$'
  if [[ ! "$user_input" =~ $_int_re ]]; then echo "invalid"; exit 1; fi
  parsed_id="$user_input"
  mysql -e "SELECT * FROM users WHERE id = $parsed_id"
}

benchmark_test_00065 "$@"
