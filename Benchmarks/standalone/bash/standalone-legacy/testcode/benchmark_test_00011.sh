#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00011() {
  user_input="`redis-cli GET user_data`"
  data=`printf "%s" "${user_input}" | tr -s " "`
  curl -s --max-time 10 -- "$data"
}

benchmark_test_00011 "$@"
