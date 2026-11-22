#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00179() {
  user_input="$(tr '&' '\n' | grep '^field=' | cut -d= -f2-)"
  mapfile -t _mapped < <(printf "%s\n" "${user_input}")
  data="${_mapped[0]}"
  checked_path="/var/app/data/$(basename -- "$data")"
  cat "$checked_path"
}

benchmark_test_00179 "$@"
