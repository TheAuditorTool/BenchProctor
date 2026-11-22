#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00058() {
  user_input="$HTTP_COOKIE"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=$(normalize "$user_input")
  xmlstarlet sel -t -v "//user[name='$data']/email" /var/data/users.xml
}

benchmark_test_00058 "$@"
