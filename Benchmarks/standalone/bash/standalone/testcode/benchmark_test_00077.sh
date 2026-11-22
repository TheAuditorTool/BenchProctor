#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00077() {
  user_input="$PATH_INFO"
  data=$(printf "%b" "${user_input//%/\\x}")
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  echo "data" > "/var/uploads/$processed"
}

benchmark_test_00077 "$@"
