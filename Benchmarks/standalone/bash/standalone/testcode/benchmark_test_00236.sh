#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00236() {
  user_input="$(jq -r '.value // empty' 2>/dev/null)"
  mapfile -t _mapped < <(printf "%s\n" "${user_input}")
  data="${_mapped[0]}"
  eval "echo $data"
}

benchmark_test_00236 "$@"
