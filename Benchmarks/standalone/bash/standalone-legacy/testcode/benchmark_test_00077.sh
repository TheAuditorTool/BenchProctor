#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00077() {
  user_input="`cat /dev/stdin`"
  data="${user_input:-default}"
  checked_path=`realpath -m "/var/app/data/$data"`
  case "$checked_path" in /var/app/data/*) ;; *) echo "forbidden" >&2; exit 1;; esac
  cat "$checked_path"
}

benchmark_test_00077 "$@"
