#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00197() {
  user_input="$HTTP_REFERER"
  printf -v data "%s" "${user_input}"
  echo "data" > "/var/uploads/$data"
}

benchmark_test_00197 "$@"
