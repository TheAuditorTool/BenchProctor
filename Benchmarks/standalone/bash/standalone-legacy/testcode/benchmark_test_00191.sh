#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00191() {
  user_input="$HTTP_USER_AGENT"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  printf '%s' "$data" | sha512sum
}

benchmark_test_00191 "$@"
