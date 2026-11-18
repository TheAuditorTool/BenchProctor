#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00127() {
  user_input="$(cat /dev/stdin)"
  mapfile -t _mapped < <(printf "%s\n" "${user_input}")
  data="${_mapped[0]}"
  eval "echo $data"
}

benchmark_test_00127 "$@"
