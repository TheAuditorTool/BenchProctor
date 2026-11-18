#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00080() {
  user_input="$HTTP_HOST"
  data="${user_input//$'\x00'/}"
  if [[ ! "$data" =~ ^-?[0-9]+$ ]]; then echo "not a number" >&2; exit 1; fi
  requested=$data
  alloc_size=$((requested + 1))
  echo "alloc:$alloc_size"
}

benchmark_test_00080 "$@"
