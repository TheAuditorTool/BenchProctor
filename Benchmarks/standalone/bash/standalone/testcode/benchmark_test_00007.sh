#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00007() {
  user_input="$HTTP_COOKIE"
  data=$(printf "%b" "${user_input//%/\\x}")
  printf '%s' "$data" | sha512sum
}

benchmark_test_00007 "$@"
