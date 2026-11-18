#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00116() {
  user_input="$(cat /dev/stdin)"
  data=$(printf "%s" "${user_input}" | tr -s " ")
  echo "data" > "/var/uploads/$data"
}

benchmark_test_00116 "$@"
