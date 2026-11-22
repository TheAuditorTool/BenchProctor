#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00176() {
  user_input="`cat /dev/stdin`"
  _captured="${user_input}"
  make_reader() { printf "%s" "$_captured" | sed 's/[[:space:]]*$//'; }
  data=`make_reader`
  if [[ ! "$data" =~ ^[0-9]{1,18}$ ]]; then echo "not a number" >&2; exit 1; fi
  record_count=$data
  (( buffer_bytes = record_count * 4096 ))
  truncate -s "$buffer_bytes" /var/app/spool/batch.buf
}

benchmark_test_00176 "$@"
