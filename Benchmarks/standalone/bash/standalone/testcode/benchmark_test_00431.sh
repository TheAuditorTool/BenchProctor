#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00431() {
  user_input="$HTTP_USER_AGENT"
  echo "data" > "/var/uploads/$user_input"
}

benchmark_test_00431 "$@"
