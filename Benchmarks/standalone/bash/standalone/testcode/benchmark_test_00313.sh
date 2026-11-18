#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00313() {
  user_input="$(sed -n 's/.*filename="\([^"]*\)".*/\1/p' | head -1)"
  data="${user_input:-default}"
  echo -n "$data" | md5sum
}

benchmark_test_00313 "$@"
