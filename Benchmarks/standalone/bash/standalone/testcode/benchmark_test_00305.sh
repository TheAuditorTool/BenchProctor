#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00305() {
  user_input="$(cat /dev/stdin)"
  mapfile -t _mapped < <(printf "%s\n" "${user_input}")
  data="${_mapped[0]}"
  rm -f "/var/app/data/$data"
}

benchmark_test_00305 "$@"
