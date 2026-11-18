#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00331() {
  user_input="$(sed -n '/^\r*$/{n;s/\r$//;p;q}')"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=$(make_reader)
  _rest="${data#*://}"
  exec 3<>"/dev/tcp/${_rest%%[/:]*}/80"
}

benchmark_test_00331 "$@"
