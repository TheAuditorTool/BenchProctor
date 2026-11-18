#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00434() {
  user_input="$(sed -n 's/.*filename="\([^"]*\)".*/\1/p' | head -1)"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=$(normalize "$user_input")
  _schema_re='^[a-zA-Z0-9 #%._-]+$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  ldapsearch -x -b "dc=example,dc=com" "uid=$processed"
}

benchmark_test_00434 "$@"
