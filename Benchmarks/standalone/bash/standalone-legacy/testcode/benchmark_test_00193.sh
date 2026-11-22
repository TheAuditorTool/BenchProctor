#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00193() {
  user_input="$HTTP_ORIGIN"
  data="${user_input:-default}"
  xsltproc --param user "'$data'" /etc/app/user_lookup.xsl /var/data/users.xml
}

benchmark_test_00193 "$@"
