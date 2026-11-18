#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00304() {
  user_input="$USER_COMMENT"
  data="${user_input//$'\x00'/}"
  echo -n "$data" | sha256sum
}

benchmark_test_00304 "$@"
