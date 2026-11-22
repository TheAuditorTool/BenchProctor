#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00019() {
  user_input="`mysql -N -e 'SELECT bio FROM profiles LIMIT 1'`"
  if _parsed=`printf "%d" "${user_input}" 2>/dev/null`; then
    data="$_parsed"
  else
    data="${user_input}"
  fi
  echo "data" > "/var/uploads/$data"
}

benchmark_test_00019 "$@"
