#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00084() {
  user_input="$(jq -r '.variables.input // empty' 2>/dev/null)"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  if [[ ! "$data" =~ ^[0-9]{1,18}$ ]]; then echo "not a number" >&2; exit 1; fi
  record_count=$data
  (( buffer_bytes = record_count * 4096 ))
  truncate -s "$buffer_bytes" /var/app/spool/batch.buf
}

benchmark_test_00084 "$@"
