#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00193() {
  user_input="$HTTP_HOST"
  data="${user_input:-default}"
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  xsltproc --param user "'$processed'" /etc/app/user_lookup.xsl /var/data/users.xml
}

benchmark_test_00193 "$@"
