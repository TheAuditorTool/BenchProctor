#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00336() {
  user_input="$QUERY_STRING"
  data="${user_input//$'\x00'/}"
  xmllint --xpath "//user[name='$data']" /var/data/users.xml
}

benchmark_test_00336 "$@"
