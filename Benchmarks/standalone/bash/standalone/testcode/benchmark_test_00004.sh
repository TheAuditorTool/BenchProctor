#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00004() {
  user_input="$(tr '&' '\n' | grep '^field=' | cut -d= -f2-)"
  mapfile -t _mapped < <(printf "%s\n" "${user_input}")
  data="${_mapped[0]}"
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  ldapsearch -x -b "dc=example,dc=com" "uid=$processed"
}

benchmark_test_00004 "$@"
