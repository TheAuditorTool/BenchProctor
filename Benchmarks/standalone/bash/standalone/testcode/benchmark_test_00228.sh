#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00228() {
  user_input="$HTTP_X_FORWARDED_FOR"
  if _parsed=$(printf "%d" "${user_input}" 2>/dev/null); then
    data="$_parsed"
  else
    data="${user_input}"
  fi
  if [[ ! "$data" =~ ^-?[0-9]+$ ]]; then echo "not a number" >&2; exit 1; fi
  requested=$data
  alloc_size=$((requested + 1))
  echo "alloc:$alloc_size"
}

benchmark_test_00228 "$@"
