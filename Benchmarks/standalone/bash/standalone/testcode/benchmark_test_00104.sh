#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00104() {
  user_input="$HTTP_ORIGIN"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  echo -n "$data" | sha256sum
}

benchmark_test_00104 "$@"
