#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00206() {
  user_input="`cat /dev/stdin`"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  printf '%s' "$data" | openssl dgst -md4 -provider legacy -provider default
}

benchmark_test_00206 "$@"
