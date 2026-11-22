#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00191() {
  user_input="$USER_COMMENT"
  data="${user_input:-default}"
  echo -n "$data" | md5sum
}

benchmark_test_00191 "$@"
