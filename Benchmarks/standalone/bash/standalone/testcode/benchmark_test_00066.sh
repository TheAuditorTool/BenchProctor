#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00066() {
  user_input="$PATH_INFO"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=$(normalize "$user_input")
  eval "echo $data"
}

benchmark_test_00066 "$@"
