#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00045() {
  user_input="$HTTP_REFERER"
  printf -v data "%s" "${user_input}"
  _rest="${data#*://}"
  exec 3<>"/dev/tcp/${_rest%%[/:]*}/80"
}

benchmark_test_00045 "$@"
