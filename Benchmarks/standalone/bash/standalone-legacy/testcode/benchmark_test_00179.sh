#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00179() {
  user_input="$HTTP_HOST"
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$user_input" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$user_input"
  rm -f "/var/app/data/$processed"
}

benchmark_test_00179 "$@"
