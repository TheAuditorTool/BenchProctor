#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00054() {
  user_input="$HTTP_COOKIE"
  printf -v data "%s" "${user_input}"
  _bool_re='^(true|false|1|0)$'
  if [[ ! "$data" =~ $_bool_re ]]; then echo "invalid bool" >&2; exit 1; fi
  parsed_bool="$data"
  xsltproc --param user "'$parsed_bool'" /etc/app/user_lookup.xsl /var/data/users.xml
}

benchmark_test_00054 "$@"
