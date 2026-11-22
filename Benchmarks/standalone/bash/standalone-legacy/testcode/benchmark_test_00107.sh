#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00107() {
  user_input="$QUERY_STRING"
  data=`echo "$user_input" | xxd -r -p 2>/dev/null || echo ""`
  _schema_re='^[a-zA-Z0-9 %._-]+$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  eval echo "~$processed"
}

benchmark_test_00107 "$@"
