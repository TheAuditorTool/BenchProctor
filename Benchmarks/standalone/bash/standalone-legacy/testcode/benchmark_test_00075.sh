#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00075() {
  user_input="$HTTP_REFERER"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  _schema_re='^[A-Za-z0-9_][A-Za-z0-9_ @-]*$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  timeout 10 sh -c "getent passwd $processed"
}

benchmark_test_00075 "$@"
