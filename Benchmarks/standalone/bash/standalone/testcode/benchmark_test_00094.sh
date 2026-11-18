#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00094() {
  user_input="$HTTP_REFERER"
  data=$(printf "%s" "${user_input}" | tr -s " ")
  rm -f "/var/app/data/$data"
}

benchmark_test_00094 "$@"
