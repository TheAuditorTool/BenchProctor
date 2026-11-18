#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00007() {
  user_input="$HTTP_AUTHORIZATION"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  echo -n "$data" | sha256sum
}

benchmark_test_00007 "$@"
