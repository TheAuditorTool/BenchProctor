#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00065() {
  user_input="$HTTP_REFERER"
  data=$(printf "%b" "${user_input//%/\\x}")
  echo "data" > "/var/uploads/$data"
}

benchmark_test_00065 "$@"
