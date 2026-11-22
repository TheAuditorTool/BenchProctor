#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00199() {
  user_input="$PATH_INFO"
  mapfile -t _mapped < <(printf "%s\n" "${user_input}")
  data="${_mapped[0]}"
  timeout 10 sh -c "getent passwd $data"
}

benchmark_test_00199 "$@"
