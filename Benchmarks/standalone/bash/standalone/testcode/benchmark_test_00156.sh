#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00156() {
  user_input="$QUERY_STRING"
  eval "echo $user_input"
}

benchmark_test_00156 "$@"
