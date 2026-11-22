#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00018() {
  user_input="$HTTP_USER_AGENT"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  reset_code="$RANDOM$RANDOM"
  echo "$reset_code"
}

benchmark_test_00018 "$@"
