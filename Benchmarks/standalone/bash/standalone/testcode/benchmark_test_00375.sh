#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00375() {
  user_input="$HTTP_COOKIE"
  data=$(echo "$user_input" | base64 -d 2>/dev/null || echo "")
  _schema_re='^[a-zA-Z0-9 #%._-]+$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  ldapsearch -x -b "dc=example,dc=com" "uid=$processed"
}

benchmark_test_00375 "$@"
