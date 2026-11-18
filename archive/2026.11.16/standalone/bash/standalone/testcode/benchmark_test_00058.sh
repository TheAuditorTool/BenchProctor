#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00058() {
  user_input="$HTTP_AUTHORIZATION"
  data="${user_input:-default}"
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  cat "/var/app/data/$processed"
}

benchmark_test_00058 "$@"
