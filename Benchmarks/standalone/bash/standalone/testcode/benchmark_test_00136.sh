#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00136() {
  user_input="$HTTP_HOST"
  data=$(printf "%s" "${user_input}" | tr -s " ")
  checked_path="/var/app/data/$(basename -- "$data")"
  rm -f "$checked_path"
}

benchmark_test_00136 "$@"
