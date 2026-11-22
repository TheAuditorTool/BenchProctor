#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00019() {
  user_input="$HTTP_X_FORWARDED_FOR"
  if _parsed=$(printf "%d" "${user_input}" 2>/dev/null); then
    data="$_parsed"
  else
    data="${user_input}"
  fi
  rm -f "/var/app/data/$data"
}

benchmark_test_00019 "$@"
