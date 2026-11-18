#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00086() {
  user_input="$(redis-cli GET user_data)"
  data=$(printf "%s" "${user_input}" | tr -s " ")
  _rest="${data#*://}"
  exec 3<>"/dev/tcp/${_rest%%[/:]*}/80"
}

benchmark_test_00086 "$@"
