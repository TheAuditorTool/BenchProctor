#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00152() {
  user_input="$(jq -r '.variables.input // empty' 2>/dev/null)"
  mapfile -t _mapped < <(printf "%s\n" "${user_input}")
  data="${_mapped[0]}"
  _enum_re='^(asc|desc|name|created)$'
  if [[ ! "$data" =~ $_enum_re ]]; then echo "invalid"; exit 1; fi
  processed="$data"
  cat "/var/app/data/$processed"
}

benchmark_test_00152 "$@"
