#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00198() {
  user_input="$(jq -r '.variables.input // empty' 2>/dev/null)"
  if _parsed=$(printf "%d" "${user_input}" 2>/dev/null); then
    data="$_parsed"
  else
    data="${user_input}"
  fi
  _url_re='^https?://[^[:space:]\]+$'
  if [[ ! "$data" =~ $_url_re ]]; then echo "forbidden host" >&2; exit 1; fi
  _authority=$(printf '%s' "$data" | sed -E 's|^[a-zA-Z]+://||; s|[/?#].*||')
  _host="${_authority%%:*}"
  _host_re='^(api\.example\.com|cdn\.example\.com)$'
  if [[ "$_authority" == *@* || ! "$_host" =~ $_host_re ]]; then echo "forbidden host" >&2; exit 1; fi
  target_url="$data"
  wget -q -O - -T 10 --max-redirect=0 -- "$target_url"
}

benchmark_test_00198 "$@"
