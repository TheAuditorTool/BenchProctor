#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00004() {
  user_input="`jq -r '.variables.input // empty' 2>/dev/null`"
  data="${user_input//$'\x00'/}"
  _schema_re='^[a-zA-Z0-9 #%._-]+$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  ldapcompare -x "uid=$processed,ou=people,dc=example,dc=com" "accountStatus:active"
}

benchmark_test_00004 "$@"
