#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00120() {
  user_input="$USER_COMMENT"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  _rest="${data#*://}"
  exec 3<>"/dev/tcp/${_rest%%[/:]*}/80"
}

benchmark_test_00120 "$@"
