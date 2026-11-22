#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00213() {
  user_input="`curl -s http://169.254.169.254/latest/meta-data/`"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  sqlite3 /var/app/data/app.db "SELECT * FROM users WHERE id = '$data'"
}

benchmark_test_00213 "$@"
