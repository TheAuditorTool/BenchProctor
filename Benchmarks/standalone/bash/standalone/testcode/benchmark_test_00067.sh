#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00067() {
  user_input="$(sed -n 's/.*filename="\([^"]*\)".*/\1/p' | head -1)"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=$(normalize "$user_input")
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  xsltproc --param user "'$processed'" /etc/app/user_lookup.xsl /var/data/users.xml
}

benchmark_test_00067 "$@"
