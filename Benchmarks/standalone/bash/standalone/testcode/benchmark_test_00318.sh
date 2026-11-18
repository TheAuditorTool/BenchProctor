#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00318() {
  user_input="$HTTP_REFERER"
  data=""
  while IFS= read -r line || [ -n "$line" ]; do data+="$line"$'\n'; done <<< "$user_input"
  data="${data%$'\n'}"
  ldapsearch -x -b "dc=example,dc=com" "uid=$data"
}

benchmark_test_00318 "$@"
