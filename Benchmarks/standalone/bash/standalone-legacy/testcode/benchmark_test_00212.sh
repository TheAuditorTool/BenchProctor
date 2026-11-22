#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00212() {
  user_input="$UPLOAD_NAME"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  checked_path=`realpath -m "/var/app/data/$data"`
  case "$checked_path" in /var/app/data/*) ;; *) echo "forbidden" >&2; exit 1;; esac
  rm -f "$checked_path"
}

benchmark_test_00212 "$@"
