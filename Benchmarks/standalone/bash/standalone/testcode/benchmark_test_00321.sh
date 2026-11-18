#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00321() {
  user_input="$(cat /dev/stdin)"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=$(make_reader)
  rm -f "/var/app/data/$data"
}

benchmark_test_00321 "$@"
