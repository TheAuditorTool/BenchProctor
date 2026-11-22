#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00110() {
  user_input="$(cat /dev/stdin)"
  data=$(printf "%s" "${user_input}" | tr -s " ")
  printf '%s' "$data" | openssl dgst -md4 -provider legacy -provider default
}

benchmark_test_00110 "$@"
