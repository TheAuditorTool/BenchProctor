#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00185() {
  user_input="$(cat /dev/stdin)"
  data=$(printf "%b" "$user_input")
  xmllint --xpath "//user[name='$data']" /var/data/users.xml
}

benchmark_test_00185 "$@"
