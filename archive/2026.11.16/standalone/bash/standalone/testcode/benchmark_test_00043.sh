#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00043() {
  user_input="$HTTP_USER_AGENT"
  data="${user_input:-default}"
  mysql -e "SELECT * FROM users WHERE id = '$data'"
}

benchmark_test_00043 "$@"
