#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00133() {
  user_input="$(sed -n 's/.*filename="\([^"]*\)".*/\1/p' | head -1)"
  mapfile -t _mapped < <(printf "%s\n" "${user_input}")
  data="${_mapped[0]}"
  _schema_re='^[a-zA-Z0-9#._-]+$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  mysql -e "SELECT * FROM users WHERE id = '$processed'"
}

benchmark_test_00133 "$@"
