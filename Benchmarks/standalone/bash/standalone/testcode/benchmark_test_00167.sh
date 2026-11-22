#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00167() {
  user_input="$(tr '&' '\n' | grep '^field=' | cut -d= -f2-)"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=$(normalize "$user_input")
  _schema_re='^[a-zA-Z0-9 %._-]+$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  timeout 10 sh -c "getent passwd $processed"
}

benchmark_test_00167 "$@"
