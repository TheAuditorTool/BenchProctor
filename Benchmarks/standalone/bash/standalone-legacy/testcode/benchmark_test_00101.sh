#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00101() {
  user_input="$HTTP_COOKIE"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=`normalize "$user_input"`
  cat "/var/app/data/$data"
}

benchmark_test_00101 "$@"
