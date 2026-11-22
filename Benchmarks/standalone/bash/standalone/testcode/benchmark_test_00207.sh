#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00207() {
  user_input="$HTTP_X_CUSTOM_HEADER"
  if _parsed=$(printf "%d" "${user_input}" 2>/dev/null); then
    data="$_parsed"
  else
    data="${user_input}"
  fi
  echo "data" > "/var/uploads/$data"
}

benchmark_test_00207 "$@"
