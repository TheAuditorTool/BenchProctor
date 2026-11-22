#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00185() {
  user_input="$USER_COMMENT"
  data=`printf "%s" "${user_input}" | tr -s " "`
  xsltproc --param user "'$data'" /etc/app/user_lookup.xsl /var/data/users.xml
}

benchmark_test_00185 "$@"
