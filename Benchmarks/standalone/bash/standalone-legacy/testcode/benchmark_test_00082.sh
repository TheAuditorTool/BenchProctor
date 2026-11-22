#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00082() {
  user_input="`tr '&' '\n' | grep '^field=' | cut -d= -f2-`"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  _int_re='^-?[0-9]+$'
  if [[ ! "$data" =~ $_int_re ]]; then echo "invalid"; exit 1; fi
  parsed_id="$data"
  psql "$DATABASE_URL" -qAt -c "PREPARE user_lookup AS SELECT * FROM users WHERE id = $parsed_id; EXECUTE user_lookup;"
}

benchmark_test_00082 "$@"
