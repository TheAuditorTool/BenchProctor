#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00029() {
  user_input="$HTTP_X_CUSTOM_HEADER"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=`make_reader`
  echo "data" > "/var/uploads/$data"
}

benchmark_test_00029 "$@"
