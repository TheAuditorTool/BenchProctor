#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00041() {
  user_input="$HTTP_X_FORWARDED_FOR"
  _schema_re='^[a-zA-Z0-9 #._~-]+$'
  if [[ ! "$user_input" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$user_input"
  cat "/var/app/data/$processed"
}

benchmark_test_00041 "$@"
