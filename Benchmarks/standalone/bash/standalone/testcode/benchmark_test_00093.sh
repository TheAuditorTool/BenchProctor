#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00093() {
  user_input="$HTTP_COOKIE"
  mapfile -t _mapped < <(printf "%s\n" "${user_input}")
  data="${_mapped[0]}"
  awk "BEGIN { srand(); print int(rand()*1000000) }"
}

benchmark_test_00093 "$@"
