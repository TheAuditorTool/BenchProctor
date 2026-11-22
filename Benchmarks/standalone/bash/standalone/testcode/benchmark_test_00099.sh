#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00099() {
  user_input="$HTTP_AUTHORIZATION"
  data="${user_input:-default}"
  ldapsearch -x -b "dc=example,dc=com" "uid=$data"
}

benchmark_test_00099 "$@"
