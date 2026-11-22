#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00070() {
  user_input="`mysql -N -e 'SELECT name FROM users LIMIT 1'`"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=`make_reader`
  printf '%s' "$data" | sha1sum
}

benchmark_test_00070 "$@"
