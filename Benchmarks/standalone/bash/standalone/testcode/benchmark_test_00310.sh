#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00310() {
  user_input="$HTTP_HOST"
  rm -f "/var/app/data/$user_input"
}

benchmark_test_00310 "$@"
