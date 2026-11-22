#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00100() {
  user_input="$HTTP_HOST"
  data=`printf "%s" "${user_input}" | tr -s " "`
  printf '%s' "$data" | sha512sum
}

benchmark_test_00100 "$@"
