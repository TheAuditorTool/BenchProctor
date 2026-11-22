#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00125() {
  user_input="$(mysql -N -e 'SELECT name FROM users LIMIT 1')"
  printf '%s' "$user_input" | sha512sum
}

benchmark_test_00125 "$@"
