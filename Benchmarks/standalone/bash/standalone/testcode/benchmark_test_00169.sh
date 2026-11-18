#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00169() {
  user_input="$(mysql -N -e 'SELECT name FROM users LIMIT 1')"
  xmllint --xpath "//user[name='$user_input']" /var/data/users.xml
}

benchmark_test_00169 "$@"
