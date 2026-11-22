#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00190() {
  user_input="$PATH_INFO"
  mysql -e "SELECT * FROM users WHERE id = '$user_input'"
}

benchmark_test_00190 "$@"
