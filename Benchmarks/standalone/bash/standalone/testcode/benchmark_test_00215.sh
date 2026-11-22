#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00215() {
  user_input="$QUERY_STRING"
  data="${user_input//$'\x00'/}"
  _schema_re='^[A-Za-z0-9_][A-Za-z0-9_ @-]*$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  eval echo "~$processed"
}

benchmark_test_00215 "$@"
