#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00010() {
  user_input="$HTTP_REFERER"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=$(normalize "$user_input")
  eval "echo $data"
}

benchmark_test_00010 "$@"
