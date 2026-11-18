#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00026() {
  user_input="$HTTP_REFERER"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=$(normalize "$user_input")
  _rest="${data#*://}"
  exec 3<>"/dev/tcp/${_rest%%[/:]*}/80"
}

benchmark_test_00026 "$@"
