#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00149() {
  user_input="$HTTP_X_FORWARDED_FOR"
  data="${user_input//$'\x00'/}"
  checked_path="/var/app/data/`basename -- "$data"`"
  echo "data" > "$checked_path"
}

benchmark_test_00149 "$@"
