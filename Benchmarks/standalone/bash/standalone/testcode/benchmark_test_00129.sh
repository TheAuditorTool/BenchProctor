#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00129() {
  user_input="$HTTP_USER_AGENT"
  data=$(printf "%s" "$user_input")
  echo -n "$data" | sha256sum
}

benchmark_test_00129 "$@"
