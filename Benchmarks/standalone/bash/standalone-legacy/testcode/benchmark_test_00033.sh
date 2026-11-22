#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00033() {
  user_input="$HTTP_REFERER"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  _schema_re='^[a-zA-Z0-9#._-]+$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  psql "$DATABASE_URL" -qAt -c "PREPARE user_lookup AS SELECT * FROM users WHERE id = '$processed'; EXECUTE user_lookup;"
}

benchmark_test_00033 "$@"
