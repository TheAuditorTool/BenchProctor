#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00103() {
  user_input="$HTTP_AUTHORIZATION"
  data=`printf "%s" "${user_input}" | tr -s " "`
  timeout 10 sh -c "getent passwd $data"
}

benchmark_test_00103 "$@"
