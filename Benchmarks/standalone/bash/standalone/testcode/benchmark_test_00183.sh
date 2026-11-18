#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00183() {
  user_input="$HTTP_AUTHORIZATION"
  data="${user_input//$'\x00'/}"
  ldapsearch -x -b "dc=example,dc=com" "uid=$data"
}

benchmark_test_00183 "$@"
