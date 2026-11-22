#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00208() {
  user_input="$(sed -n '/^\r*$/{n;s/\r$//;p;q}')"
  printf -v data "%s" "${user_input}"
  echo -n "$data" | sha256sum
}

benchmark_test_00208 "$@"
