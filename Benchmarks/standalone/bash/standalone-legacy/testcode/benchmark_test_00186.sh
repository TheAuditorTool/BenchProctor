#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00186() {
  user_input="$APP_INPUT"
  printf -v data "%s" "${user_input}"
  xmllint --xpath "//user[name='$data']" /var/data/users.xml
}

benchmark_test_00186 "$@"
