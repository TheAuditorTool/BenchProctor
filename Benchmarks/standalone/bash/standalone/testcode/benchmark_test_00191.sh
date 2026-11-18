#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00191() {
  user_input="$(jq -r '.value // empty' 2>/dev/null)"
  mysql -e "SELECT * FROM users WHERE id = '$user_input'"
}

benchmark_test_00191 "$@"
