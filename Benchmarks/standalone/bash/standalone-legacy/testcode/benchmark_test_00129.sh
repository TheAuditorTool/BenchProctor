#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00129() {
  user_input="$PATH_INFO"
  data=`printf "%s" "$user_input"`
  reset_code="$RANDOM$RANDOM"
  echo "$reset_code"
}

benchmark_test_00129 "$@"
