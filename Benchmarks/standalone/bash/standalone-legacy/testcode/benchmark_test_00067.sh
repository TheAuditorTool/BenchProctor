#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00067() {
  user_input="`jq -r '.value // empty' 2>/dev/null`"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  _schema_re='^[a-zA-Z0-9 %._~-]+$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  xmlstarlet sel -t -v "//user[name='$processed']/email" /var/data/users.xml
}

benchmark_test_00067 "$@"
