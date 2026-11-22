#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00167() {
  user_input="`tr '&' '\n' | grep '^field=' | cut -d= -f2-`"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=`make_reader`
  timeout 10 sh -c "getent passwd $data"
}

benchmark_test_00167 "$@"
