#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00197() {
  user_input="$(jq -r '.value // empty' 2>/dev/null)"
  printf -v data "%s" "${user_input}"
  echo "data" > "/var/uploads/$data"
}

benchmark_test_00197 "$@"
