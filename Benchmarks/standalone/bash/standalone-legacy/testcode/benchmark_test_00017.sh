#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00017() {
  user_input="`jq -r '.variables.input // empty' 2>/dev/null`"
  data=`printf "%s" "$user_input"`
  reset_code=`uuidgen --time`
  echo "$reset_code"
}

benchmark_test_00017 "$@"
