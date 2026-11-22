#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00100() {
  user_input="$QUERY_STRING"
  echo -n "$user_input" | md5sum
}

benchmark_test_00100 "$@"
