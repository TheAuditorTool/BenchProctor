#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00132() {
  user_input="$1"
  if _parsed=$(printf "%d" "${user_input}" 2>/dev/null); then
    data="$_parsed"
  else
    data="${user_input}"
  fi
  _schema_re='^[a-zA-Z0-9 #._~-]+$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  rm -f "/var/app/data/$processed"
}

benchmark_test_00132 "$@"
