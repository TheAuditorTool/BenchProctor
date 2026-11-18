#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00006() {
  user_input="$(sed -n 's/.*filename="\([^"]*\)".*/\1/p' | head -1)"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  _schema_re='^[A-Za-z0-9_][A-Za-z0-9_ @-]*$'
  if [[ ! "$data" =~ $_schema_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  ldapsearch -x -b "dc=example,dc=com" "uid=$processed"
}

benchmark_test_00006 "$@"
