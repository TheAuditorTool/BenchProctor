#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00069() {
  user_input="$(sed -n '/^\r*$/{n;s/\r$//;p;q}')"
  data="${user_input//$'\x00'/}"
  echo -n "$data" | md5sum
}

benchmark_test_00069 "$@"
