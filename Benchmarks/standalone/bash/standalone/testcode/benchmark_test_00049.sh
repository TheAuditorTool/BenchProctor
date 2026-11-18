#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00049() {
  user_input="$PATH_INFO"
  data="${user_input//$'\x00'/}"
  awk "BEGIN { srand(); print int(rand()*1000000) }"
}

benchmark_test_00049 "$@"
