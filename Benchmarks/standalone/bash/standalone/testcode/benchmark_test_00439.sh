#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00439() {
  user_input="$APP_INPUT"
  data="${user_input:-default}"
  mysql -e "SELECT * FROM users WHERE id = '$data'"
}

benchmark_test_00439 "$@"
