#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00126() {
  user_input="$(sed -n 's/.*filename="\([^"]*\)".*/\1/p' | head -1)"
  mysql -e "SELECT * FROM users WHERE id = '$user_input'"
}

benchmark_test_00126 "$@"
