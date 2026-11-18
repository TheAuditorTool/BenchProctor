#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00062() {
  user_input="$(jq -r '.value // empty' 2>/dev/null)"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  echo "data" > "/var/uploads/$data"
}

benchmark_test_00062 "$@"
