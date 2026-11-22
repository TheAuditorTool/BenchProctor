#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00031() {
  user_input="$HTTP_ORIGIN"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=$(normalize "$user_input")
  if [[ ! "$data" =~ ^[0-9]{1,18}$ ]]; then echo "not a number" >&2; exit 1; fi
  record_count=$data
  (( buffer_bytes = record_count * 4096 ))
  truncate -s "$buffer_bytes" /var/app/spool/batch.buf
}

benchmark_test_00031 "$@"
