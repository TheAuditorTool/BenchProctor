#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00419() {
  user_input="$PATH_INFO"
  mapfile -t _mapped < <(printf "%s\n" "${user_input}")
  data="${_mapped[0]}"
  _bool_re='^(true|false|1|0)$'
  if [[ ! "$data" =~ $_bool_re ]]; then echo "invalid bool" >&2; exit 1; fi
  parsed_bool="$data"
  xmllint --xpath "//user[name='$parsed_bool']" /var/data/users.xml
}

benchmark_test_00419 "$@"
