#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00159() {
  user_input="$HTTP_REFERER"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  _schema_re='^[a-zA-Z0-9#._-]+$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  mysql -e "SELECT * FROM users WHERE id = '$processed'"
}

benchmark_test_00159 "$@"
