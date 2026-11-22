#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00037() {
  user_input="$HTTP_REFERER"
  mapfile -t _mapped < <(printf "%s\n" "${user_input}")
  data="${_mapped[0]}"
  if [[ ! "$data" =~ ^[0-9]{1,18}$ ]]; then echo "not a number" >&2; exit 1; fi
  quantity=$data
  local -i total_cents=quantity*1299
  printf 'order total: %d cents\n' "$total_cents"
}

benchmark_test_00037 "$@"
