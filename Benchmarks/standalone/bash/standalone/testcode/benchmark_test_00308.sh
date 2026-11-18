#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00308() {
  user_input="$PATH_INFO"
  data=$(printf "%b" "${user_input//%/\\x}")
  printf "%s" "$data" | openssl enc -des-ede3-cbc -K "$DATA_ENC_KEY" -iv "$(openssl rand -hex 8)" -out /var/app/run/record.enc
}

benchmark_test_00308 "$@"
