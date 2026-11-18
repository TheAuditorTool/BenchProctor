#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00028() {
  user_input="$(cat /dev/stdin)"
  data=$(printf "%s" "${user_input}" | tr -s " ")
  echo -n "$data" | sha256sum
}

benchmark_test_00028 "$@"
