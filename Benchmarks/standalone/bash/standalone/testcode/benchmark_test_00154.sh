#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00154() {
  user_input="$(tr '&' '\n' | grep '^field=' | cut -d= -f2-)"
  mapfile -t _mapped < <(printf "%s\n" "${user_input}")
  data="${_mapped[0]}"
  echo "data" > "/var/uploads/$data"
}

benchmark_test_00154 "$@"
