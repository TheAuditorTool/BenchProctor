#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00002() {
  user_input="$PATH_INFO"
  data=`printf "%s" "$user_input"`
  echo -n "$data" | md5sum
}

benchmark_test_00002 "$@"
