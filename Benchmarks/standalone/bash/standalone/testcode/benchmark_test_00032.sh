#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00032() {
  user_input="$HTTP_ORIGIN"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=$(make_reader)
  printf "%s" "$data" | openssl enc -des-ede3-cbc -K "$DATA_ENC_KEY" -iv "$(openssl rand -hex 8)" -out /var/app/run/record.enc
}

benchmark_test_00032 "$@"
