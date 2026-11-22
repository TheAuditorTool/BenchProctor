#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00211() {
  user_input="$HTTP_REFERER"
  data=$(printf "%b" "${user_input//%/\\x}")
  awk -v name="$data" 'BEGIN { system("getent group " name) }'
}

benchmark_test_00211 "$@"
