#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00028() {
  user_input="$(jq -r '.value // empty' 2>/dev/null)"
  data=$(echo "$user_input" | jq -r '.value // empty' 2>/dev/null || echo "")
  case $data in /bin/echo|/bin/cat|/usr/bin/id) allowed_bin=$data;; *) echo "forbidden binary" >&2; exit 1;; esac
  eval "$allowed_bin"
}

benchmark_test_00028 "$@"
