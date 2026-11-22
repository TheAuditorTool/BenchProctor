#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00065() {
  user_input="`cat /dev/stdin`"
  data=`echo "$user_input" | jq -r '.value // empty' 2>/dev/null || echo ""`
  _rest="${data#*://}"
  exec 3<>"/dev/tcp/${_rest%%[/:]*}/80"
}

benchmark_test_00065 "$@"
