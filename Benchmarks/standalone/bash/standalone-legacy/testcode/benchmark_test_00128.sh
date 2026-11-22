#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00128() {
  user_input="`cat /dev/stdin`"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  _rest="${data#*://}"
  exec 3<>"/dev/tcp/${_rest%%[/:]*}/80"
}

benchmark_test_00128 "$@"
