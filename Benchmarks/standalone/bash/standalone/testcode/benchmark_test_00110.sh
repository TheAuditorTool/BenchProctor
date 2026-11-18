#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00110() {
  user_input="$(cat /dev/stdin)"
  data="${user_input//$'\x00'/}"
  cat "/var/app/data/$data"
}

benchmark_test_00110 "$@"
