#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00005() {
  user_input="$HTTP_HOST"
  data="${user_input//$'\x00'/}"
  curl -s --max-time 10 -- "$data"
}

benchmark_test_00005 "$@"
