#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00018() {
  user_input="$(cat /dev/stdin)"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  _schema_re='^[A-Za-z0-9_][A-Za-z0-9_ @-]*$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  eval "echo $processed"
}

benchmark_test_00018 "$@"
