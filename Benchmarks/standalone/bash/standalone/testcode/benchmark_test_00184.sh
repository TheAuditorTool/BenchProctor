#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00184() {
  user_input="$(tr '&' '\n' | grep '^field=' | cut -d= -f2-)"
  data=$(printf "%s" "${user_input}" | tr -s " ")
  echo -n "$data" | md5sum
}

benchmark_test_00184 "$@"
