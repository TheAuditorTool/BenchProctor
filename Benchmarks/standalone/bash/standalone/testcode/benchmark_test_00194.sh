#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00194() {
  user_input="$PATH_INFO"
  if [[ ! "$user_input" =~ ^[0-9]{1,18}$ ]]; then echo "not a number" >&2; exit 1; fi
  record_count=$user_input
  (( buffer_bytes = record_count * 4096 ))
  truncate -s "$buffer_bytes" /var/app/spool/batch.buf
}

benchmark_test_00194 "$@"
