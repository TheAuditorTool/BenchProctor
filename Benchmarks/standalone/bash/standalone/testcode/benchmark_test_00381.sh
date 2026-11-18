#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00381() {
  user_input="$(jq -r '.value // empty' 2>/dev/null)"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  _int_re='^-?[0-9]+$'
  if [[ ! "$data" =~ $_int_re ]]; then echo "invalid"; exit 1; fi
  parsed_id="$data"
  mysql -e "SELECT * FROM users WHERE id = $parsed_id"
}

benchmark_test_00381 "$@"
