#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00205() {
  user_input="$HTTP_USER_AGENT"
  mysql -e "SELECT * FROM users WHERE id = '$user_input'"
}

benchmark_test_00205 "$@"
