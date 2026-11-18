#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00244() {
  user_input="$(tr '&' '\n' | grep '^field=' | cut -d= -f2-)"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  _schema_re='^[a-zA-Z0-9 %._-]+$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  eval "echo $processed"
}

benchmark_test_00244 "$@"
