#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00048() {
  user_input="`cat /dev/stdin`"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=`make_reader`
  printf '%s' "$data" | xmllint --stream --noent --nonet -
}

benchmark_test_00048 "$@"
