#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00254() {
  user_input="$PATH_INFO"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  _schema_re='^[a-zA-Z0-9 #._~-]+$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  rm -f "/var/app/data/$processed"
}

benchmark_test_00254 "$@"
