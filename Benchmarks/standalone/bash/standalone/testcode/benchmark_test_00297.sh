#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00297() {
  user_input="$HTTP_X_FORWARDED_FOR"
  if _parsed=$(printf "%d" "${user_input}" 2>/dev/null); then
    data="$_parsed"
  else
    data="${user_input}"
  fi
  xmllint --xpath "//user[name='$data']" /var/data/users.xml
}

benchmark_test_00297 "$@"
