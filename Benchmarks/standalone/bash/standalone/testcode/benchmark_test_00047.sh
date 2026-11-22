#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00047() {
  user_input="$(jq -r '.value // empty' 2>/dev/null)"
  printf -v data "%s" "${user_input}"
  _rest="${data#*://}"
  exec 3<>"/dev/tcp/${_rest%%[/:]*}/80"
}

benchmark_test_00047 "$@"
