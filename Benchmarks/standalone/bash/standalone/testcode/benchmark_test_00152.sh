#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00152() {
  user_input="$(mysql -N -e 'SELECT name FROM users LIMIT 1')"
  data=$(printf "%s" "$user_input")
  printf '%s' "$data" | openssl enc -aes-256-ecb -pbkdf2 -iter 600000 -pass env:DATA_ENC_KEY -out /var/app/run/record.enc
}

benchmark_test_00152 "$@"
