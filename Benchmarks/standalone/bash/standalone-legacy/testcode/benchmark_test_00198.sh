#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00198() {
  user_input="`sed -n 's/.*filename="\([^"]*\)".*/\1/p' | head -1`"
  _first_line() { IFS= read -r _line; printf '%s' "$_line"; }
  data=`printf "%s\n" "${user_input}" | _first_line`
  _url_re='^https?://[^[:space:]\]+$'
  if [[ ! "$data" =~ $_url_re ]]; then echo "forbidden host" >&2; exit 1; fi
  _authority=`printf '%s' "$data" | sed -E 's|^[a-zA-Z]+://||; s|[/?#].*||'`
  _host="${_authority%%:*}"
  _host_re='^(api\.example\.com|cdn\.example\.com)$'
  case "$_authority" in *@*) echo "forbidden host" >&2; exit 1;; esac
  if [[ ! "$_host" =~ $_host_re ]]; then echo "forbidden host" >&2; exit 1; fi
  target_url="$data"
  _rest="${target_url#*://}"
  exec 3<>"/dev/tcp/${_rest%%[/:]*}/80"
}

benchmark_test_00198 "$@"
