#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00195() {
  user_input="$(sed -n '/^\r*$/{n;s/\r$//;p;q}')"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  echo -n "$data" | sha256sum
}

benchmark_test_00195 "$@"
