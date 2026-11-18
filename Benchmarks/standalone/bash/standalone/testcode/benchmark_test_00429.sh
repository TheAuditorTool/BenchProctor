#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00429() {
  user_input="$(sed -n 's/.*filename="\([^"]*\)".*/\1/p' | head -1)"
  data="${user_input//$'\x00'/}"
  _schema_re='^[a-zA-Z0-9 #._~-]+$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  echo "data" > "/var/uploads/$processed"
}

benchmark_test_00429 "$@"
