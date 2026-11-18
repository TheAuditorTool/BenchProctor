#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00085() {
  user_input="$(sed -n '/^\r*$/{n;s/\r$//;p;q}')"
  if _parsed=$(printf "%d" "${user_input}" 2>/dev/null); then
    data="$_parsed"
  else
    data="${user_input}"
  fi
  echo "$data" | xmllint --noent --nonet - > /dev/null 2>&1
}

benchmark_test_00085 "$@"
