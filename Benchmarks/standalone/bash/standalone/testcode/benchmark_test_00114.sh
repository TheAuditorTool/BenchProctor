#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00114() {
  user_input="$(jq -r '.value // empty' 2>/dev/null)"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=$(make_reader)
  awk -v name="$data" 'BEGIN { system("getent group " name) }'
}

benchmark_test_00114 "$@"
