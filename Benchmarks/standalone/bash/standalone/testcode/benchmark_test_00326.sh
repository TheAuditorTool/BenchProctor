#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00326() {
  user_input="$HTTP_REFERER"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  echo -n "$data" | md5sum
}

benchmark_test_00326 "$@"
