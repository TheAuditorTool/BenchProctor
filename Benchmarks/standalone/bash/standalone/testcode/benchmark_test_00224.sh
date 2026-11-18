#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00224() {
  user_input="$HTTP_AUTHORIZATION"
  data=$(echo "$user_input" | base64 -d 2>/dev/null || echo "")
  if [[ ! "$data" =~ ^-?[0-9]+$ ]]; then echo "not a number" >&2; exit 1; fi
  requested=$data
  alloc_size=$((requested + 1))
  echo "alloc:$alloc_size"
}

benchmark_test_00224 "$@"
