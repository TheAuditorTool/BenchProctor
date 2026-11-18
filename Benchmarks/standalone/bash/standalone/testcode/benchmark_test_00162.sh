#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00162() {
  user_input="$HTTP_REFERER"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  eval "echo $data"
}

benchmark_test_00162 "$@"
