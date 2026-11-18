#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00013() {
  user_input="$HTTP_REFERER"
  data="${user_input:-default}"
  awk "BEGIN { srand(); print int(rand()*1000000) }"
}

benchmark_test_00013 "$@"
