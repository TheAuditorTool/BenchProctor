#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00038() {
  user_input="$(jq -r '.value // empty' 2>/dev/null)"
  data=$(echo "$user_input" | jq -r '.value // empty' 2>/dev/null || echo "")
  _schema_re='^[A-Za-z0-9_][A-Za-z0-9_ @-]*$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  ldapsearch -x -b "dc=example,dc=com" "uid=$processed"
}

benchmark_test_00038 "$@"
