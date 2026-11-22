#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00196() {
  user_input="$APP_INPUT"
  data=$(printf "%s" "$user_input")
  reset_code=$(uuidgen --time)
  echo "$reset_code"
}

benchmark_test_00196 "$@"
