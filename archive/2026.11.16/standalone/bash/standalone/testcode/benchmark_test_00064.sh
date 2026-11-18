#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00064() {
  user_input="$HTTP_X_FORWARDED_FOR"
  data=$(printf "%s" "${user_input}" | tr -s " ")
  cat "/var/app/data/$data"
}

benchmark_test_00064 "$@"
