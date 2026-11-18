#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00021() {
  user_input="$QUERY_STRING"
  data=$(printf "%s" "$user_input")
  eval "echo $data"
}

benchmark_test_00021 "$@"
