#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00171() {
  user_input="$HTTP_COOKIE"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=$(normalize "$user_input")
  checked_path="/var/app/data/$(basename -- "$data")"
  cat "$checked_path"
}

benchmark_test_00171 "$@"
