#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00333() {
  user_input="$QUERY_STRING"
  data=$(printf "%s" "${user_input}" | tr -s " ")
  echo -n "$data" | sha256sum
}

benchmark_test_00333 "$@"
