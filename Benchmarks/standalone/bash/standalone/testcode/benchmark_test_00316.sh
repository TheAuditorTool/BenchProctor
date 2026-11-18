#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00316() {
  user_input="$(cat /dev/stdin)"
  data="${user_input:-default}"
  echo -n "$data" | md5sum
}

benchmark_test_00316 "$@"
