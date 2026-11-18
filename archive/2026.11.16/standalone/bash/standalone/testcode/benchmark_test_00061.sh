#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00061() {
  user_input="$PATH_INFO"
  data=$(printf "%s" "${user_input}" | tr -s " ")
  xmllint --xpath "//user[name='$data']" /var/data/users.xml
}

benchmark_test_00061 "$@"
