#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00005() {
  user_input="$(sed -n '/^\r*$/{n;s/\r$//;p;q}')"
  data=$(printf "%b" "${user_input//%/\\x}")
  xmllint --xpath "//user[name='$data']" /var/data/users.xml
}

benchmark_test_00005 "$@"
