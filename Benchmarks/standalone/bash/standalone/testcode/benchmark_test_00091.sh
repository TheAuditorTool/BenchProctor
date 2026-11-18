#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00091() {
  user_input="$HTTP_ORIGIN"
  data=$(printf "%s" "$user_input")
  xmllint --xpath "//user[name='$data']" /var/data/users.xml
}

benchmark_test_00091 "$@"
