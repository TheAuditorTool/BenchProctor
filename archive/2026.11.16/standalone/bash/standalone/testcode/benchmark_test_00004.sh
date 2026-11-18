#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00004() {
  user_input="$HTTP_HOST"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  printf "%s" "$data" | openssl enc -des-ede3-cbc -K "$DATA_ENC_KEY" -iv "$(openssl rand -hex 8)" -out /var/app/run/record.enc
}

benchmark_test_00004 "$@"
