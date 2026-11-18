#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00018() {
  user_input="$HTTP_HOST"
  data=$(printf "%s" "$user_input")
  echo -n "$data" | md5sum
}

benchmark_test_00018 "$@"
