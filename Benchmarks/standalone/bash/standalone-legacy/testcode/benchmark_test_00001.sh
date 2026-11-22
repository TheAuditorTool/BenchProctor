#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00001() {
  user_input="$HTTP_REFERER"
  printf -v data "%s" "${user_input}"
  wget -q -O - -T 10 --max-redirect=0 -- "$data"
}

benchmark_test_00001 "$@"
