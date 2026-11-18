#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00293() {
  user_input="$(mysql -N -e 'SELECT name FROM users LIMIT 1')"
  data=$(printf "%s" "$user_input")
  printf "%s" "$data" | openssl enc -des-ede3-cbc -K "$DATA_ENC_KEY" -iv "$(openssl rand -hex 8)" -out /var/app/run/record.enc
}

benchmark_test_00293 "$@"
