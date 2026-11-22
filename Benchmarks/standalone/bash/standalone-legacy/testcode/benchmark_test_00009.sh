#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00009() {
  user_input="$1"
  data="${user_input//$'\x00'/}"
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  cat "/var/app/data/$processed"
}

benchmark_test_00009 "$@"
