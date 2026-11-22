#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00076() {
  user_input="$QUERY_STRING"
  printf -v data "%s" "${user_input}"
  echo -n "$data" | sha256sum
}

benchmark_test_00076 "$@"
