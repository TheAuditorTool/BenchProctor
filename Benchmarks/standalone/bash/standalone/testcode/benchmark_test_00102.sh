#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00102() {
  user_input="$(mysql -N -e 'SELECT name FROM users LIMIT 1')"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  cat "/var/app/data/$data"
}

benchmark_test_00102 "$@"
