#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00130() {
  user_input="$HTTP_COOKIE"
  data="${user_input:-default}"
  xmllint --xpath "//user[name='$data']" /var/data/users.xml
}

benchmark_test_00130 "$@"
