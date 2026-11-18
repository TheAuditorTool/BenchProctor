#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00031() {
  user_input="$(curl -s http://169.254.169.254/latest/meta-data/)"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  mysql -e "SELECT * FROM users WHERE id = '$data'"
}

benchmark_test_00031 "$@"
