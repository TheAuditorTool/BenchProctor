#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00327() {
  user_input="$HTTP_ORIGIN"
  printf -v data "%s" "${user_input}"
  cat "/var/app/data/$data"
}

benchmark_test_00327 "$@"
