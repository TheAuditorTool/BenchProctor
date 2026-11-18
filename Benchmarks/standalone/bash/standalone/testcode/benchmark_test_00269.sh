#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00269() {
  user_input="$(sed -n '/^\r*$/{n;s/\r$//;p;q}')"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  echo -n "$data" | md5sum
}

benchmark_test_00269 "$@"
