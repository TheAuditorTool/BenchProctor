#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00068() {
  user_input="$(tr '&' '\n' | grep '^field=' | cut -d= -f2-)"
  data="${user_input:-default}"
  xmllint --xpath "//user[name='$data']" /var/data/users.xml
}

benchmark_test_00068 "$@"
