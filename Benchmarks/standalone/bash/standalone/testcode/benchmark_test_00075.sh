#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00075() {
  user_input="$HTTP_USER_AGENT"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  case $data in /bin/echo|/bin/cat|/usr/bin/id) allowed_bin=$data;; *) echo "forbidden binary" >&2; exit 1;; esac
  eval "$allowed_bin"
}

benchmark_test_00075 "$@"
