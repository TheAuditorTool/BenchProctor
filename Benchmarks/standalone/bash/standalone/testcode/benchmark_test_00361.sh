#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00361() {
  user_input="$HTTP_COOKIE"
  data=$(printf "%s" "${user_input}" | tr -s " ")
  eval "echo $data"
}

benchmark_test_00361 "$@"
