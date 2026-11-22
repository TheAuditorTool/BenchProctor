#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00180() {
  user_input="$HTTP_X_CUSTOM_HEADER"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  psql "$DATABASE_URL" -qAt -c "PREPARE user_lookup AS SELECT * FROM users WHERE id = '$data'; EXECUTE user_lookup;"
}

benchmark_test_00180 "$@"
