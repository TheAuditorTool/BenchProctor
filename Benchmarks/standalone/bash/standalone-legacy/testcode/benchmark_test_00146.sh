#!/bin/bash
# SPDX-License-Identifier: Apache-2.0

benchmark_test_00146() {
  user_input="`curl -s http://169.254.169.254/latest/meta-data/`"
  data="${user_input//$'\x00'/}"
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

benchmark_test_00146 "$@"
