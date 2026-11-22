#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00009() {
  user_input="$1"
  data="${user_input//$'\x00'/}"
  cat "/var/app/data/$data"
}

benchmark_test_00009 "$@"
