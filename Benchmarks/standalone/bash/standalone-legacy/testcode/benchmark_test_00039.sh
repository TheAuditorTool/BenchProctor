#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00039() {
  user_input="$USER_COMMENT"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  coerced_float=`printf "%.6f" "$data" 2>/dev/null` || { echo "invalid float" >&2; exit 1; }
  xsltproc --param user "'$coerced_float'" /etc/app/user_lookup.xsl /var/data/users.xml
}

benchmark_test_00039 "$@"
