#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00183() {
  user_input="`mysql -N -e 'SELECT name FROM users LIMIT 1'`"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=`normalize "$user_input"`
  xsltproc --param user "'$data'" /etc/app/user_lookup.xsl /var/data/users.xml
}

benchmark_test_00183 "$@"
