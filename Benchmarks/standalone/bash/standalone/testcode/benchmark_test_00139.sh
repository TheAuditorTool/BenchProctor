#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00139() {
  user_input="$HTTP_COOKIE"
  data=$(echo "$user_input" | xxd -r -p 2>/dev/null || echo "")
  _rest="${data#*://}"
  exec 3<>"/dev/tcp/${_rest%%[/:]*}/80"
}

benchmark_test_00139 "$@"
