#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00165() {
  user_input="$HTTP_COOKIE"
  _schema_re='^[A-Za-z0-9_][A-Za-z0-9_ @-]*$'
  if [[ ! "$user_input" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$user_input"
  eval "echo $processed"
}

benchmark_test_00165 "$@"
