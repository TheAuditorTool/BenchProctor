#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00168() {
  user_input="$HTTP_HOST"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  echo -n "$data" | md5sum
}

benchmark_test_00168 "$@"
