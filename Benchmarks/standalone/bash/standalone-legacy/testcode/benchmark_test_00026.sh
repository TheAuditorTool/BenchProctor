#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00026() {
  user_input="$HTTP_HOST"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  checked_path="/var/app/data/`basename -- "$data"`"
  cat "$checked_path"
}

benchmark_test_00026 "$@"
