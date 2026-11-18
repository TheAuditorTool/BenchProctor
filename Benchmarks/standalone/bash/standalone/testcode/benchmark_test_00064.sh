#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00064() {
  user_input="$HTTP_HOST"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=$(make_reader)
  _schema_re='^[a-zA-Z0-9 %._~-]+$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  xmllint --xpath "//user[name='$processed']" /var/data/users.xml
}

benchmark_test_00064 "$@"
