#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00289() {
  user_input="$APP_INPUT"
  data=""
  IFS="," read -ra _tokens <<< "${user_input}"
  for token in "${_tokens[@]}"; do data="$token"; done
  case $data in /bin/echo|/bin/cat|/usr/bin/id) allowed_bin=$data;; *) echo "forbidden binary" >&2; exit 1;; esac
  eval "$allowed_bin"
}

benchmark_test_00289 "$@"
