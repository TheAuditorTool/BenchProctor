#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00149() {
  user_input="$PATH_INFO"
  mapfile -t _mapped < <(printf "%s\n" "${user_input}")
  data="${_mapped[0]}"
  cat "/var/app/data/$data"
}

benchmark_test_00149 "$@"
