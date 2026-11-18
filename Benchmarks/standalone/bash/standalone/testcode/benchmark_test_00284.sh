#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00284() {
  user_input="$(cat /dev/stdin)"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=$(make_reader)
  _schema_re='^[a-zA-Z0-9#._-]+$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  mysql -e "SELECT * FROM users WHERE id = '$processed'"
}

benchmark_test_00284 "$@"
