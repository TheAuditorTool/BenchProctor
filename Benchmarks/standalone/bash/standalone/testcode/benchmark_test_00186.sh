#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00186() {
  user_input="$HTTP_COOKIE"
  xmlstarlet sel -t -v "//user[name='$user_input']/email" /var/data/users.xml
}

benchmark_test_00186 "$@"
