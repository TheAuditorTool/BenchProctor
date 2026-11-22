#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00045() {
  user_input="$(sed -n 's/.*filename="\([^"]*\)".*/\1/p' | head -1)"
  data=$(printf "%s" "$user_input")
  xmllint --xpath "//user[name='$data']" /var/data/users.xml
}

benchmark_test_00045 "$@"
