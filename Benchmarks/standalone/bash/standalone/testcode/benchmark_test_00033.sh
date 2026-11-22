#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00033() {
  user_input="$HTTP_USER_AGENT"
  sqlite3 /var/app/data/app.db "SELECT * FROM users WHERE id = '$user_input'"
}

benchmark_test_00033 "$@"
