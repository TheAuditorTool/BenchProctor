#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00363() {
  user_input="$HTTP_ORIGIN"
  data=""
  while IFS= read -r line || [ -n "$line" ]; do data+="$line"$'\n'; done <<< "$user_input"
  data="${data%$'\n'}"
  xmllint --xpath "//user[name='$data']" /var/data/users.xml
}

benchmark_test_00363 "$@"
