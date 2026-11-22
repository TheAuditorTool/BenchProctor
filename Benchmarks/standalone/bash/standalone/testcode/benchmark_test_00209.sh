#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00209() {
  user_input="$(sed -n '/^\r*$/{n;s/\r$//;p;q}')"
  rm -f "/var/app/data/$user_input"
}

benchmark_test_00209 "$@"
