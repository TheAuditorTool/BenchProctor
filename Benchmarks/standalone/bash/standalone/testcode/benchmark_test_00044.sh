#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00044() {
  user_input="$APP_INPUT"
  data="${user_input:-default}"
  _schema_re='^[A-Za-z0-9_][A-Za-z0-9_ @-]*$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  eval "echo $processed"
}

benchmark_test_00044 "$@"
