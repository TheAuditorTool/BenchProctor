#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00071() {
  user_input="$(cat /dev/stdin)"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  xmllint --xpath "//user[name='$data']" /var/data/users.xml
}

benchmark_test_00071 "$@"
