#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00073() {
  user_input="$HTTP_ORIGIN"
  if _parsed=`printf "%d" "${user_input}" 2>/dev/null`; then
    data="$_parsed"
  else
    data="${user_input}"
  fi
  reset_code=`uuidgen --time`
  echo "$reset_code"
}

benchmark_test_00073 "$@"
