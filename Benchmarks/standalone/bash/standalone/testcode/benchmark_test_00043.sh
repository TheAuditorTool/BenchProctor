#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00043() {
  user_input="$HTTP_X_FORWARDED_FOR"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  printf "%s" "$data" | openssl enc -des-ede3-cbc -K "$DATA_ENC_KEY" -iv "$(openssl rand -hex 8)" -out /var/app/run/record.enc
}

benchmark_test_00043 "$@"
