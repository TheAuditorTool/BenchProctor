#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00002() {
  user_input="$HTTP_REFERER"
  printf -v data "%s" "${user_input}"
  printf '%s' "$data" | openssl dgst -sha3-256
}

benchmark_test_00002 "$@"
