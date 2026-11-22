#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00200() {
  user_input="`redis-cli GET user_data`"
  data="${user_input:-default}"
  wget -q -O - -T 10 --max-redirect=0 -- "$data"
}

benchmark_test_00200 "$@"
