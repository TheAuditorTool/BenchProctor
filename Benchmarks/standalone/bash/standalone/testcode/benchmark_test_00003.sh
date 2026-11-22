#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00003() {
  user_input="$PATH_INFO"
  data=$(printf "%b" "${user_input//%/\\x}")
  _schema_re='^[a-zA-Z0-9#._-]+$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  mysql -e "SELECT * FROM users WHERE id = '$processed'"
}

benchmark_test_00003 "$@"
