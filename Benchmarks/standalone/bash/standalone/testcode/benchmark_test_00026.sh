#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00026() {
  user_input="$(jq -r '.variables.input // empty' 2>/dev/null)"
  if _parsed=$(printf "%d" "${user_input}" 2>/dev/null); then
    data="$_parsed"
  else
    data="${user_input}"
  fi
  echo "data" > "/var/uploads/$data"
}

benchmark_test_00026 "$@"
