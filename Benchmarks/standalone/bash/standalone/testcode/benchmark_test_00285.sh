#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00285() {
  user_input="$(jq -r '.variables.input // empty' 2>/dev/null)"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  echo -n "$data" | md5sum
}

benchmark_test_00285 "$@"
