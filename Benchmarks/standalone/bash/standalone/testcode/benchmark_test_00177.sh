#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00177() {
  user_input="$(cat /dev/stdin)"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  curl -s --max-time 10 -- "$data"
}

benchmark_test_00177 "$@"
