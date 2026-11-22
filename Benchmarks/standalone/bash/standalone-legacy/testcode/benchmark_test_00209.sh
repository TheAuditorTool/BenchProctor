#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00209() {
  user_input="$HTTP_USER_AGENT"
  if _parsed=`printf "%d" "${user_input}" 2>/dev/null`; then
    data="$_parsed"
  else
    data="${user_input}"
  fi
  checked_path=`realpath -m "/var/app/data/$data"`
  case "$checked_path" in /var/app/data/*) ;; *) echo "forbidden"; exit 1;; esac
  echo "data" > "$checked_path"
}

benchmark_test_00209 "$@"
