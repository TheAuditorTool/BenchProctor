#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00199() {
  user_input="$HTTP_X_CUSTOM_HEADER"
  data="${user_input:-default}"
  _schema_re='^[a-zA-Z0-9 #%._-]+$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  ldapsearch -x -b "dc=example,dc=com" "uid=$processed"
}

benchmark_test_00199 "$@"
