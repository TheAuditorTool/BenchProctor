#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00020() {
  user_input="`mysql -N -e 'SELECT name FROM users LIMIT 1'`"
  data="${user_input:-default}"
  xmlstarlet sel -t -v "//user[name='$data']/email" /var/data/users.xml
}

benchmark_test_00020 "$@"
