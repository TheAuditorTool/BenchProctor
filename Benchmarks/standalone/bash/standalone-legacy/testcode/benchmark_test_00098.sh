#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00098() {
  user_input="$HTTP_X_CUSTOM_HEADER"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  _schema_re='^[a-zA-Z0-9 #._~-]+$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  echo "data" > "/var/uploads/$processed"
}

benchmark_test_00098 "$@"
