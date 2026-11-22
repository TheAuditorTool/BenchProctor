#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00103() {
  user_input="$APP_INPUT"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  _schema_re='^[A-Za-z0-9_][A-Za-z0-9_ @-]*$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  awk -v name="$processed" 'BEGIN { system("getent group " name) }'
}

benchmark_test_00103 "$@"
