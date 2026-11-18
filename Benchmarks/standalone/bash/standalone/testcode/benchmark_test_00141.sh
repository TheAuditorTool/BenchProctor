#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00141() {
  user_input="$(cat /dev/stdin)"
  data="${user_input//$'\x00'/}"
  curl -s "$data"
}

benchmark_test_00141 "$@"
