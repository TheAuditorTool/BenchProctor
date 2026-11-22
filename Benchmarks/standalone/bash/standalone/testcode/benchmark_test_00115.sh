#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00115() {
  user_input="$HTTP_USER_AGENT"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=$(make_reader)
  printf '%s' "$data" | openssl dgst -sha3-256
}

benchmark_test_00115 "$@"
