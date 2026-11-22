#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00176() {
  user_input="$HTTP_X_FORWARDED_FOR"
  mapfile -t _mapped < <(printf "%s\n" "${user_input}")
  data="${_mapped[0]}"
  if [[ ! "$data" =~ ^-?[0-9]+$ ]]; then echo "not a number" >&2; exit 1; fi
  requested=$data
  alloc_size=$((requested + 1))
  echo "alloc:$alloc_size"
}

benchmark_test_00176 "$@"
