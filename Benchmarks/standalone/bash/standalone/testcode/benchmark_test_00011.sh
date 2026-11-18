#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00011() {
  user_input="$(mysql -N -e 'SELECT name FROM users LIMIT 1')"
  data=$(printf "%s" "$user_input")
  xmllint --xpath "//user[name='$data']" /var/data/users.xml
}

benchmark_test_00011 "$@"
