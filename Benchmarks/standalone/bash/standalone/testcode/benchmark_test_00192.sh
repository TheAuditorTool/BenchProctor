#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00192() {
  user_input="$PATH_INFO"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=$(make_reader)
  xmllint --xpath "//user[name='$data']" /var/data/users.xml
}

benchmark_test_00192 "$@"
