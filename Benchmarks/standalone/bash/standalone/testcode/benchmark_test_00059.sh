#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00059() {
  user_input="$HTTP_REFERER"
  if _parsed=$(printf "%d" "${user_input}" 2>/dev/null); then
    data="$_parsed"
  else
    data="${user_input}"
  fi
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  xmlstarlet sel -t -v "//user[name='$processed']/email" /var/data/users.xml
}

benchmark_test_00059 "$@"
