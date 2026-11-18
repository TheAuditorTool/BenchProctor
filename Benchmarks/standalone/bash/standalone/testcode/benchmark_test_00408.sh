#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00408() {
  user_input="$PATH_INFO"
  data=""
  while IFS= read -r line || [ -n "$line" ]; do data+="$line"$'\n'; done <<< "$user_input"
  data="${data%$'\n'}"
  xmllint --xpath "//user[name='$data']" /var/data/users.xml
}

benchmark_test_00408 "$@"
