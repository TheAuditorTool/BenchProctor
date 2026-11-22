#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00079() {
  user_input="$1"
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$user_input" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$user_input"
  awk -v name="$processed" 'BEGIN { system("getent group " name) }'
}

benchmark_test_00079 "$@"
