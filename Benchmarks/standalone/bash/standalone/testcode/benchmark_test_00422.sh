#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00422() {
  user_input="$HTTP_COOKIE"
  data=$(printf "%s" "$user_input")
  eval "echo $data"
}

benchmark_test_00422 "$@"
