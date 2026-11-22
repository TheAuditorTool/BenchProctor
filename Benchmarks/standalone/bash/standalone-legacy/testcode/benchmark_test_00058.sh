#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00058() {
  user_input="`jq -r '.variables.input // empty' 2>/dev/null`"
  printf -v data "%s" "${user_input}"
  xmlstarlet sel -t -v "//user[name='$data']/email" /var/data/users.xml
}

benchmark_test_00058 "$@"
