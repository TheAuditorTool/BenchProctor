#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00130() {
  user_input="$(cat /dev/stdin)"
  _url_re='^https?://[^[:space:]\]+$'
  if [[ ! "$user_input" =~ $_url_re ]]; then echo "forbidden host" >&2; exit 1; fi
  _authority=$(printf '%s' "$user_input" | sed -E 's|^[a-zA-Z]+://||; s|[/?#].*||')
  _host="${_authority%%:*}"
  _host_re='^(api\.example\.com|cdn\.example\.com)$'
  if [[ "$_authority" == *@* || ! "$_host" =~ $_host_re ]]; then echo "forbidden host" >&2; exit 1; fi
  target_url="$user_input"
  wget -q -O - -T 10 --max-redirect=0 -- "$target_url"
}

benchmark_test_00130 "$@"
