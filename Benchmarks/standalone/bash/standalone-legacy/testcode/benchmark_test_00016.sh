#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00016() {
  user_input="$HTTP_X_CUSTOM_HEADER"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  printf '%s' "$data" | sha512sum
}

benchmark_test_00016 "$@"
