#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00066() {
  user_input="$PATH_INFO"
  data="${user_input:-default}"
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  eval echo "~$processed"
}

benchmark_test_00066 "$@"
