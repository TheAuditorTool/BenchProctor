#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00034() {
  user_input="$HTTP_HOST"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=$(normalize "$user_input")
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  ldapsearch -x -b "dc=example,dc=com" "uid=$processed"
}

benchmark_test_00034 "$@"
