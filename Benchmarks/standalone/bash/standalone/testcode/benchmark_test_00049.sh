#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00049() {
  user_input="$HTTP_REFERER"
  wget -q -O - -T 10 --max-redirect=0 -- "$user_input"
}

benchmark_test_00049 "$@"
