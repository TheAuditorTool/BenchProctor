#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00035() {
  user_input="$(jq -r '.value // empty' 2>/dev/null)"
  data="${user_input:-default}"
  eval "echo $data"
}

benchmark_test_00035 "$@"
