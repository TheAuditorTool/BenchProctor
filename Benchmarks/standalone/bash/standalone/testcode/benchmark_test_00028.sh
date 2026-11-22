#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00028() {
  user_input="$1"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=$(make_reader)
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  timeout 10 sh -c "getent passwd $processed"
}

benchmark_test_00028 "$@"
