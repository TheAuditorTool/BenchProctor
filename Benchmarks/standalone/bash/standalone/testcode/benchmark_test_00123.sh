#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00123() {
  user_input="$HTTP_COOKIE"
  normalize() { local _v="$1"; printf "%s" "$_v" | tr -d "\r\n"; }
  data=$(normalize "$user_input")
  _host=$(echo "$data" | sed -E "s#^[a-zA-Z]+://##; s#[/:].*##")
  _host_re='^(api\.example\.com|cdn\.example\.com)$'
  if [[ ! "$_host" =~ $_host_re ]]; then echo "forbidden host" >&2; exit 1; fi
  target_url="$data"
  curl -s "$target_url"
}

benchmark_test_00123 "$@"
