#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00159() {
  user_input="$HTTP_AUTHORIZATION"
  if [ -n "$user_input" ]; then data="$user_input"; else data=""; fi
  _url_re='^https?://[^[:space:]\]+$'
  if [[ ! "$data" =~ $_url_re ]]; then echo "forbidden host" >&2; exit 1; fi
  _authority=$(printf '%s' "$data" | sed -E 's|^[a-zA-Z]+://||; s|[/?#].*||')
  _host="${_authority%%:*}"
  _host_re='^(api\.example\.com|cdn\.example\.com)$'
  if [[ "$_authority" == *@* || ! "$_host" =~ $_host_re ]]; then echo "forbidden host" >&2; exit 1; fi
  target_url="$data"
  curl -s --max-time 10 -- "$target_url"
}

benchmark_test_00159 "$@"
