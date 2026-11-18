#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00052() {
  user_input="$HTTP_ORIGIN"
  if _parsed=$(printf "%d" "${user_input}" 2>/dev/null); then
    data="$_parsed"
  else
    data="${user_input}"
  fi
  cat "/var/app/data/$data"
}

benchmark_test_00052 "$@"
