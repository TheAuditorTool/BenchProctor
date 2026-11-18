#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00095() {
  user_input="$(cat /dev/stdin)"
  _host=$(echo "$user_input" | sed -E "s#^[a-zA-Z]+://##; s#[/:].*##")
  _host_re='^(api\.example\.com|cdn\.example\.com)$'
  if [[ ! "$_host" =~ $_host_re ]]; then echo "forbidden host" >&2; exit 1; fi
  target_url="$user_input"
  curl -s "$target_url"
}

benchmark_test_00095 "$@"
