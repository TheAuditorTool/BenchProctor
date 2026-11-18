#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00005() {
  user_input="$(cat /dev/stdin)"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  _schema_re='^[a-zA-Z0-9 %._~-]+$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  xmllint --xpath "//user[name='$processed']" /var/data/users.xml
}

benchmark_test_00005 "$@"
