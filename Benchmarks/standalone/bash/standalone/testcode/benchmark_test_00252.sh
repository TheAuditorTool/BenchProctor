#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00252() {
  user_input="$(tr '&' '\n' | grep '^field=' | cut -d= -f2-)"
  data="${user_input//$'\x00'/}"
  eval "echo $data"
}

benchmark_test_00252 "$@"
