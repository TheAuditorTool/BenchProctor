#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00202() {
  user_input="$PATH_INFO"
  data=$(printf "%s" "$user_input")
  _schema_re='^[a-zA-Z0-9 %._-]+$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  eval "echo $processed"
}

benchmark_test_00202 "$@"
