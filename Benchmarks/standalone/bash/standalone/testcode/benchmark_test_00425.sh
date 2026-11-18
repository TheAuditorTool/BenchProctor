#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00425() {
  user_input="$HTTP_AUTHORIZATION"
  data=$(printf "%s" "${user_input}" | tr -s " ")
  echo -n "$data" | sha256sum
}

benchmark_test_00425 "$@"
