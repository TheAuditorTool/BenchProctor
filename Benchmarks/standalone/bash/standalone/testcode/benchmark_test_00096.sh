#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00096() {
  user_input="$QUERY_STRING"
  data=$(echo "$user_input" | xxd -r -p 2>/dev/null || echo "")
  xsltproc --param user "'$data'" /etc/app/user_lookup.xsl /var/data/users.xml
}

benchmark_test_00096 "$@"
