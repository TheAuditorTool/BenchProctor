#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00225() {
  user_input="$HTTP_REFERER"
  if _parsed=$(printf "%d" "${user_input}" 2>/dev/null); then
    data="$_parsed"
  else
    data="${user_input}"
  fi
  curl -s "$data"
}

benchmark_test_00225 "$@"
