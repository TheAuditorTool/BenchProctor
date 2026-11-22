#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00157() {
  user_input="`jq -r '.value // empty' 2>/dev/null`"
  printf -v data "%s" "${user_input}"
  printf '%s' "$data" | openssl dgst -md4 -provider legacy -provider default
}

benchmark_test_00157 "$@"
