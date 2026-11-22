#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00208() {
  user_input="`jq -r '.variables.input // empty' 2>/dev/null`"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=`make_reader`
  echo -n "$data" | sha256sum
}

benchmark_test_00208 "$@"
