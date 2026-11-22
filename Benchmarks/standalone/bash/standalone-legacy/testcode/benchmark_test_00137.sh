#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00137() {
  user_input="`jq -r '.variables.input // empty' 2>/dev/null`"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  if [[ ! "$data" =~ ^-?[0-9]+$ ]]; then echo "not a number" >&2; exit 1; fi
  requested=$data
  alloc_size=$((requested + 1))
  echo "alloc:$alloc_size"
}

benchmark_test_00137 "$@"
