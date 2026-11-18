#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00076() {
  user_input="$(sed -n 's/.*filename="\([^"]*\)".*/\1/p' | head -1)"
  data="${user_input//$'\x00'/}"
  echo -n "$data" | sha256sum
}

benchmark_test_00076 "$@"
