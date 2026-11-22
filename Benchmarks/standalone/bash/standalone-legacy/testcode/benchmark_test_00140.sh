#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00140() {
  user_input="$PATH_INFO"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  ldapsearch -x -b "dc=example,dc=com" "uid=$data"
}

benchmark_test_00140 "$@"
