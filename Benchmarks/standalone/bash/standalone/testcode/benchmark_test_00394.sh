#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00394() {
  user_input="$PATH_INFO"
  data=$(printf "%s" "$user_input")
  eval "echo $data"
}

benchmark_test_00394 "$@"
