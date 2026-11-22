#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00220() {
  user_input="$APP_INPUT"
  data=$(printf "%s" "${user_input}" | tr -s " ")
  awk -v name="$data" 'BEGIN { system("getent group " name) }'
}

benchmark_test_00220 "$@"
