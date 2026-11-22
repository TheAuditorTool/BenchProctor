#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00129() {
  user_input="$HTTP_ORIGIN"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  reset_code=$(uuidgen --time)
  echo "$reset_code"
}

benchmark_test_00129 "$@"
