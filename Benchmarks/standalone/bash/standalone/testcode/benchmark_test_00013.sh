#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00013() {
  user_input="$HTTP_HOST"
  printf -v data "%s" "${user_input}"
  printf '%s' "$data" | sha1sum
}

benchmark_test_00013 "$@"
