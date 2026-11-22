#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00043() {
  user_input="`cat /dev/stdin`"
  data=""
  while IFS= read -r line || [ -n "$line" ]; do data+="$line"$'\n'; done <<< "$user_input"
  data="${data%$'\n'}"
  checked_path=`realpath -m "/var/app/data/$data"`
  case "$checked_path" in /var/app/data/*) ;; *) echo "forbidden" >&2; exit 1;; esac
  rm -f "$checked_path"
}

benchmark_test_00043 "$@"
