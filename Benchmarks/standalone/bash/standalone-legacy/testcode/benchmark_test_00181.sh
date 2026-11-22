#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00181() {
  user_input="`tr '&' '\n' | grep '^field=' | cut -d= -f2-`"
  data=`printf "%s" "${user_input}" | tr -s " "`
  awk -v name="$data" 'BEGIN { system("getent group " name) }'
}

benchmark_test_00181 "$@"
