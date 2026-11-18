#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00077() {
  user_input="$HTTP_AUTHORIZATION"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=$(normalize "$user_input")
  xmllint --xpath "//user[name='$data']" /var/data/users.xml
}

benchmark_test_00077 "$@"
