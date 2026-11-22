#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00166() {
  user_input="$PATH_INFO"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  sqlite3 /var/app/data/app.db "SELECT * FROM users WHERE id = '$data'"
}

benchmark_test_00166 "$@"
