#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00391() {
  user_input="$HTTP_COOKIE"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=$(make_reader)
  mysql -e "SELECT * FROM users WHERE id = '$data'"
}

benchmark_test_00391 "$@"
