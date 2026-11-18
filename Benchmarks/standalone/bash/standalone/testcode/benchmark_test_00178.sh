#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00178() {
  user_input="$HTTP_AUTHORIZATION"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  awk "BEGIN { srand(); print int(rand()*1000000) }"
}

benchmark_test_00178 "$@"
