#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00184() {
  user_input="$HTTP_X_CUSTOM_HEADER"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=$(make_reader)
  wget -q -O - -T 10 --max-redirect=0 -- "$data"
}

benchmark_test_00184 "$@"
