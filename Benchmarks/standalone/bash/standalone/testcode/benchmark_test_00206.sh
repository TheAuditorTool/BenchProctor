#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00206() {
  user_input="$HTTP_X_FORWARDED_FOR"
  data="${user_input:-default}"
  printf '%s' "$data" | sha1sum
}

benchmark_test_00206 "$@"
