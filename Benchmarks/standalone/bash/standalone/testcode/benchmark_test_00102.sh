#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00102() {
  user_input="$HTTP_ORIGIN"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  xmllint --xpath "//user[name='$data']" /var/data/users.xml
}

benchmark_test_00102 "$@"
