#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00127() {
  user_input="`jq -r '.value // empty' 2>/dev/null`"
  data="${user_input:-default}"
  coerced_float=`printf "%.6f" "$data" 2>/dev/null` || { echo "invalid float" >&2; exit 1; }
  xsltproc --param user "'$coerced_float'" /etc/app/user_lookup.xsl /var/data/users.xml
}

benchmark_test_00127 "$@"
