#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00436() {
  user_input="$(jq -r '.value // empty' 2>/dev/null)"
  data=$(echo "$user_input" | jq -r '.value // empty' 2>/dev/null || echo "")
  xmllint --xpath "//user[name='$data']" /var/data/users.xml
}

benchmark_test_00436 "$@"
