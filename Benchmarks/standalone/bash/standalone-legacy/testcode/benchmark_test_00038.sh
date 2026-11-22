#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00038() {
  user_input="$HTTP_X_FORWARDED_FOR"
  data="${user_input//$'\x00'/}"
  cat "/var/app/data/$data"
}

benchmark_test_00038 "$@"
