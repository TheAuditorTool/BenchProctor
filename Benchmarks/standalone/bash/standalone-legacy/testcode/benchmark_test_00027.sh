#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00027() {
  user_input="$HTTP_REFERER"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=`make_reader`
  awk -v name="$data" 'BEGIN { system("getent group " name) }'
}

benchmark_test_00027 "$@"
