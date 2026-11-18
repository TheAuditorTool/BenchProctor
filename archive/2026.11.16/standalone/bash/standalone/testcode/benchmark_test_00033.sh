#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00033() {
  user_input="$HTTP_X_FORWARDED_FOR"
  mapfile -t _mapped < <(printf "%s\n" "${user_input}")
  data="${_mapped[0]}"
  printf "%s" "$data" | openssl enc -des-ede3-cbc -K "$DATA_ENC_KEY" -iv "$(openssl rand -hex 8)" -out /var/app/run/record.enc
}

benchmark_test_00033 "$@"
