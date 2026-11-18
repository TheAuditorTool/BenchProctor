#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00070() {
  user_input="$HTTP_ORIGIN"
  data=$(printf "%s" "$user_input")
  echo -n "$data" | md5sum
}

benchmark_test_00070 "$@"
