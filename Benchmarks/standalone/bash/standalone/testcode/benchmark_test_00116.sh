#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00116() {
  user_input="$(cat /dev/stdin)"
  if _parsed=$(printf "%d" "${user_input}" 2>/dev/null); then
    data="$_parsed"
  else
    data="${user_input}"
  fi
  printf '%s' "$data" | openssl dgst -sha3-256
}

benchmark_test_00116 "$@"
