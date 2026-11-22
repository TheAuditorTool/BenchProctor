#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00016() {
  user_input="$(sed -n '/^\r*$/{n;s/\r$//;p;q}')"
  data="${user_input:-default}"
  echo -n "$data" | sha256sum
}

benchmark_test_00016 "$@"
