#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00187() {
  user_input="$(mysql -N -e 'SELECT name FROM users LIMIT 1')"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=$(make_reader)
  ldapsearch -x -b "dc=example,dc=com" "uid=$data"
}

benchmark_test_00187 "$@"
