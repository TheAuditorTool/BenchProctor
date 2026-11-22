#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00078() {
  user_input="$HTTP_HOST"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  xsltproc --param user "'$data'" /etc/app/user_lookup.xsl /var/data/users.xml
}

benchmark_test_00078 "$@"
