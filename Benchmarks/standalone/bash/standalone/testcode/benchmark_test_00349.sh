#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00349() {
  user_input="$HTTP_REFERER"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  mysql -e "SELECT * FROM users WHERE id = '$data'"
}

benchmark_test_00349 "$@"
