#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00172() {
  user_input="$HTTP_COOKIE"
  mapfile -t _mapped < <(printf "%s\n" "${user_input}")
  data="${_mapped[0]}"
  _rest="${data#*://}"
  exec 3<>"/dev/tcp/${_rest%%[/:]*}/80"
}

benchmark_test_00172 "$@"
