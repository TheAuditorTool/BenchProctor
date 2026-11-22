#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00156() {
  user_input="$USER_COMMENT"
  data="${user_input:-default}"
  mysql -e "SELECT * FROM users WHERE id = '$data'"
}

benchmark_test_00156 "$@"
