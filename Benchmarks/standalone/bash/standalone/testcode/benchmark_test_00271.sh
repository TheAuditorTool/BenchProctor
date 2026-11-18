#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00271() {
  user_input="$(sed -n 's/.*filename="\([^"]*\)".*/\1/p' | head -1)"
  data=$(printf "%s" "${user_input}" | tr -s " ")
  printf "%s" "$data" | openssl enc -des-ede3-cbc -K "$DATA_ENC_KEY" -iv "$(openssl rand -hex 8)" -out /var/app/run/record.enc
}

benchmark_test_00271 "$@"
