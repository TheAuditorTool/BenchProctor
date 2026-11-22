#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00181() {
  user_input="$HTTP_AUTHORIZATION"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=$(normalize "$user_input")
  timeout 10 sh -c "getent passwd $data"
}

benchmark_test_00181 "$@"
