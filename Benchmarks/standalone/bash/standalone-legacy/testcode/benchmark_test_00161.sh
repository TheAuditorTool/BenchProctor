#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00161() {
  user_input="$HTTP_REFERER"
  data=""
  while IFS= read -r line || [ -n "$line" ]; do data+="$line"$'\n'; done <<< "$user_input"
  data="${data%$'\n'}"
  if [[ ! "$data" =~ ^-?[0-9]+$ ]]; then echo "invalid"; exit 1; fi
  bounded_val="$data"
  if [ "$bounded_val" -lt 0 ] || [ "$bounded_val" -gt 2147483647 ]; then echo "out of range" >&2; exit 1; fi
  if [[ ! "$bounded_val" =~ ^[0-9]{1,18}$ ]]; then echo "not a number" >&2; exit 1; fi
  record_count=$bounded_val
  if (( record_count > 1048576 )); then echo "batch too large" >&2; exit 1; fi
  (( buffer_bytes = record_count * 4096 ))
  truncate -s "$buffer_bytes" /var/app/spool/batch.buf
}

benchmark_test_00161 "$@"
