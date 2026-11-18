#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00019() {
  user_input="$APP_INPUT"
  mapfile -t _mapped < <(printf "%s\n" "${user_input}")
  data="${_mapped[0]}"
  ldapsearch -x -b "dc=example,dc=com" "uid=$data"
}

benchmark_test_00019 "$@"
