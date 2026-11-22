#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00109() {
  user_input="`sed -n 's/.*filename="\([^"]*\)".*/\1/p' | head -1`"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=`normalize "$user_input"`
  ldapsearch -x -b "dc=example,dc=com" "uid=$data"
}

benchmark_test_00109 "$@"
