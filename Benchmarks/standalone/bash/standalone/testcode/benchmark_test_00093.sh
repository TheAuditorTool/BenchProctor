#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00093() {
  user_input="$HTTP_AUTHORIZATION"
  data="${user_input//$'\x00'/}"
  timeout 10 sh -c "getent passwd $data"
}

benchmark_test_00093 "$@"
