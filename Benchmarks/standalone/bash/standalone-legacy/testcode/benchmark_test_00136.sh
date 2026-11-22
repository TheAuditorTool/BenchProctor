#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00136() {
  user_input="`sed -n '/^\r*$/{n;s/\r$//;p;q}'`"
  data=`printf "%b" "${user_input//%/\\\x}"`
  cat "/var/app/data/$data"
}

benchmark_test_00136 "$@"
