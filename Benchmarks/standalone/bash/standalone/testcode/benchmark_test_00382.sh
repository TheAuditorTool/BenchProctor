#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00382() {
  user_input="$PATH_INFO"
  data="${user_input:-default}"
  echo -n "$data" | md5sum
}

benchmark_test_00382 "$@"
