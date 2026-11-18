#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00428() {
  user_input="$HTTP_USER_AGENT"
  data=$(printf "%s" "${user_input}" | tr -s " ")
  printf "%s" "$data" | openssl enc -des-ede3-cbc -K "$DATA_ENC_KEY" -iv "$(openssl rand -hex 8)" -out /var/app/run/record.enc
}

benchmark_test_00428 "$@"
