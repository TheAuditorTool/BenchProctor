#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00233() {
  user_input="$(sed -n '/^\r*$/{n;s/\r$//;p;q}')"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=$(normalize "$user_input")
  echo "$data" | xmllint --noent --nonet - > /dev/null 2>&1
}

benchmark_test_00233 "$@"
