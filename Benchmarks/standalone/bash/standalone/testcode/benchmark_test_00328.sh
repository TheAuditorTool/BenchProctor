#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00328() {
  user_input="$HTTP_COOKIE"
  if _parsed=$(printf "%d" "${user_input}" 2>/dev/null); then
    data="$_parsed"
  else
    data="${user_input}"
  fi
  _host=$(echo "$data" | sed -E "s#^[a-zA-Z]+://##; s#[/:].*##")
  _host_re='^(api\.example\.com|cdn\.example\.com)$'
  if [[ ! "$_host" =~ $_host_re ]]; then echo "forbidden host" >&2; exit 1; fi
  target_url="$data"
  curl -s "$target_url"
}

benchmark_test_00328 "$@"
