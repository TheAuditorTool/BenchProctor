#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00117() {
  user_input="$QUERY_STRING"
  data="${user_input:-default}"
  echo -n "$data" | sha256sum
}

benchmark_test_00117 "$@"
