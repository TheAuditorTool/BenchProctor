#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00003() {
  user_input="`tr '&' '\n' | grep '^field=' | cut -d= -f2-`"
  data="${user_input:-default}"
  mysql -e "SELECT * FROM users WHERE id = '$data'"
}

benchmark_test_00003 "$@"
