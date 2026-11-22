#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00142() {
  user_input="`jq -r '.variables.input // empty' 2>/dev/null`"
  printf -v data "%s" "${user_input}"
  printf '%s' "$data" | sha1sum
}

benchmark_test_00142 "$@"
