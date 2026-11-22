#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00065() {
  user_input="$(cat /dev/stdin)"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=$(make_reader)
  wget -q -O - -T 10 --max-redirect=0 -- "$data"
}

benchmark_test_00065 "$@"
